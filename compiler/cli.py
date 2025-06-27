import io
import os
import sys
from collections import defaultdict

import requests

from compiler.compiler import Compiler, filename_by_classname
from compiler.parser import TlFileParser
from compiler.templates import (
    FUNCTION_CLASS_DEFENITION,
    OBJECT_CLASS_DEFINITION,
    TLOBJECT_CLASS_DEFINITION,
)
from compiler.types import ClassDefinition

RAW_FILE_LINK = "https://raw.githubusercontent.com/tdlib/td/refs/heads/master/td/generate/scheme/td_api.tl"


def write_existed_file(output_path: str, text: str):
    with open(output_path, "w") as file:
        file.write(text)


def main():
    args = sys.argv
    if len(args) < 2:
        print(f"Usage: {args[0]} output_path")
        print(
            "Creates types based on https://github.com/tdlib/td/blob/master/td/generate/scheme/td_api.tl"
        )
        return
    output_path = args[1]
    os.makedirs(output_path, exist_ok=True)

    tl_scheme_file = requests.get(RAW_FILE_LINK)
    input_file = io.StringIO(tl_scheme_file.text)

    # Skip builtin definition
    lines = 0
    while lines < 13:
        if input_file.read(1) == "\n":
            lines += 1

    parser = TlFileParser(input_file)
    childrens = defaultdict(list)
    while current_part := parser.read_part():
        if (
            isinstance(current_part, ClassDefinition)
            and current_part.parent
            and current_part.parent.lower() != current_part.class_name.lower()
        ):
            current_part.class_name = (
                current_part.class_name[0].upper() + current_part.class_name[1:]
            )
            childrens[current_part.parent].append(current_part.class_name)

    input_file = io.StringIO(tl_scheme_file.text)

    # Skip builtin definition
    lines = 0
    while lines < 13:
        if input_file.read(1) == "\n":
            lines += 1
    parser = TlFileParser(input_file)

    compiler = Compiler()
    compiler.childrens = childrens
    while class_definition := parser.read_part():
        text = compiler.convert_object_to_class(class_definition)
        filename = filename_by_classname(class_definition.class_name)
        save_path = os.path.join(output_path, filename + ".py")
        with open(save_path, "w") as file:
            file.write(text)

        pyi_text = compiler.convert_object_to_class(class_definition, with_types=True)
        save_path = os.path.join(output_path, filename + ".pyi")
        with open(save_path, "w") as file:
            file.write(pyi_text)

    write_existed_file(
        os.path.join(output_path, "tl_object.py"), TLOBJECT_CLASS_DEFINITION
    )

    write_existed_file(
        os.path.join(output_path, "function.py"), FUNCTION_CLASS_DEFENITION
    )

    write_existed_file(
        os.path.join(output_path, "object_base.py"), OBJECT_CLASS_DEFINITION
    )


if __name__ == "__main__":
    main()
