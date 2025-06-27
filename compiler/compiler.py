import builtins
import copy
import keyword
import re
import textwrap
from collections import defaultdict
from dataclasses import dataclass

from compiler.templates import CLASS_TEMPLATE, FUNCTION_TEMPLATE
from compiler.types import (
    BaseObject,
    ClassArgument,
    ClassDefinition,
    FunctionDefinition,
)

BUILTIN_DATATYPES = {
    "double": "float",
    "string": "str",
    "int32": "int",
    "int53": "int",
    "int64": "int",
    "bytes": "bytes",
    "Bool": "bool",
}

BUILTIN_DEFAULT_VALUES = {
    "float": "0",
    "int": "0",
    "str": '""',
    "bool": "False",
    "bytes": 'b""',
}
TAB_SPACES = "    "
DO_NOT_USE_NAMES = frozenset(dir(builtins) + list(keyword.kwlist))

# https://stackoverflow.com/questions/1175208/elegant-python-function-to-convert-camelcase-to-snake-case
CAMEL_TO_SNAKE_REGEX = re.compile(r"(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])")

VECTOR_TYPE_REGEX = re.compile(r"^vector<(.+)>$")

PREDEFINED_IMPORTS = {"List": "from typing import List"}


@dataclass
class Argument:
    name: str
    type_: str
    default: str


def filename_by_classname(name: str):
    return CAMEL_TO_SNAKE_REGEX.sub("_", name).lower()


def relative_import_from_file(class_name: str):
    if class_name in PREDEFINED_IMPORTS:
        return PREDEFINED_IMPORTS[class_name]
    filename = filename_by_classname(class_name)
    return f"from .{filename} import {class_name}"


# TODO: Refactor?
# TODO: Make function to detect default argument based on description
class Compiler:
    def __init__(self) -> None:
        self.aliases = {}
        self.childrens = defaultdict(list)

    def _get_vector_type(self, arg_type: str, imported_classes: set):
        match = VECTOR_TYPE_REGEX.match(arg_type)
        if not match:
            raise ValueError(f"Wrong vector: {arg_type}")

        arg_type = self._process_argument_type(
            match.group(1), imported_classes, inside_vector=True
        )
        imported_classes.add("List")

        return f"List[{arg_type}]"

    def _process_argument_type(
        self, arg_type: str, imported_classes: set[str], inside_vector: bool = False
    ):
        if arg_type in BUILTIN_DATATYPES:
            arg_type = BUILTIN_DATATYPES[arg_type]
        elif arg_type.startswith("vector"):
            arg_type = self._get_vector_type(arg_type, imported_classes)
            if not inside_vector:
                arg_type += " | None"
        else:
            if arg_type in self.aliases:
                arg_type = self.aliases[arg_type]
            imported_classes.add(arg_type)
            if not inside_vector:
                arg_type += " | None"

        return arg_type

    def prepare_arguments(
        self, data_arguments: list[ClassArgument], with_types: bool
    ) -> tuple[list[Argument], set[str]]:
        arguments = []
        imported_classes = set()
        for arg in data_arguments:
            if with_types:
                arg_type = self._process_argument_type(arg.type_, imported_classes)
            else:
                arg_type = ""
            default_value = BUILTIN_DEFAULT_VALUES.get(arg_type, "None")
            arguments.append(Argument(arg.name, arg_type, default_value))

        return arguments, imported_classes

    def prepare_imports(self, imported_classes: set[str]):
        imports = []
        for class_name in imported_classes:
            import_path = relative_import_from_file(class_name)
            imports.append(import_path)

        imports.sort()
        return imports

    def prepare_docs(self, data: BaseObject):
        docs = ['"""']
        if data.description:
            docs.append(data.description)

        docs.append("")  # newline

        for arg in data.arguments:
            if arg.description:
                docs.append(f":param {arg.name}: {arg.description}")

        if isinstance(data, FunctionDefinition):
            docs.append(f":return: :class:`{data.return_type}`")

        docs.append('"""')

        return docs

    def prepare_slots(self, arguments: list[Argument]):
        argument_names = [a.name for a in arguments] + ["_extra", "_client_id", "_type"]
        return (
            TAB_SPACES
            + "__slots__ = ("
            + ", ".join(f'"{a}"' for a in argument_names)
            + ")"
        )

    def create_init_function(
        self, arguments: list[Argument], class_extra_name: str, with_types: bool
    ):
        arguments_text = ["self"] + [
            (f"{a.name}: {a.type_} = {a.default}")
            if with_types
            else f"{a.name} = {a.default}"
            for a in arguments
        ]
        arguments_text = ", ".join(arguments_text)
        set_commands = (
            "\n".join(f"{TAB_SPACES * 2}self.{a.name} = {a.name}" for a in arguments)
            + f'\n{TAB_SPACES * 2}self._type = "{class_extra_name}"'
        )
        return f"{TAB_SPACES}def __init__({arguments_text}):\n{set_commands}"

    def convert_object_to_class(self, data: BaseObject, with_types: bool = False):
        data = copy.copy(data)
        arguments, imported_classes = self.prepare_arguments(data.arguments, with_types)
        aliases = self.aliases
        class_extra_type = data.class_name

        if isinstance(data, ClassDefinition):
            if data.parent is None:
                data.parent = "ObjectBase"
            elif data.class_name.lower() == data.parent.lower():
                aliases[data.class_name] = data.parent
                data.class_name = data.parent
                data.parent = "ObjectBase"
            else:
                data.class_name = data.class_name[0].upper() + data.class_name[1:]

            imported_classes.add(data.parent)

        if isinstance(data, FunctionDefinition):
            data.class_name = data.class_name[0].upper() + data.class_name[1:]
            if data.return_type in aliases:
                data.return_type = aliases[data.return_type]
            if data.return_type in self.childrens:
                childrens = self.childrens[data.return_type]
                data.return_type = " | ".join(childrens)
                imported_classes.update(childrens)
            else:
                imported_classes.add(data.return_type)

        for i in imported_classes:
            assert " " not in i

        if with_types:
            imports = self.prepare_imports(imported_classes)
        elif isinstance(data, ClassDefinition):
            imports = self.prepare_imports({data.parent})  # type: ignore
        else:
            imports = set()
        imports_text = "\n".join(imports)

        docs = self.prepare_docs(data)
        docs_text = textwrap.indent("\n".join(docs), "    ")

        slots_text = self.prepare_slots(arguments)
        init_function_text = self.create_init_function(
            arguments, class_extra_type, with_types
        )

        if isinstance(data, ClassDefinition):
            return CLASS_TEMPLATE.format(
                imports=imports_text,
                class_name=data.class_name,
                parent=data.parent,
                docstring=docs_text,
                slots=slots_text,
                init_function=init_function_text,
            )
        elif isinstance(data, FunctionDefinition):
            return_type = f"[{data.return_type}]" if with_types else ""
            return FUNCTION_TEMPLATE.format(
                imports=imports_text,
                class_name=data.class_name,
                ret_type=data.return_type,
                docstring=docs_text,
                slots=slots_text,
                init_function=init_function_text,
                return_type=return_type,
            )
        else:
            raise TypeError(f"Unknown type for data: {type(data)}")
