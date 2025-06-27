import pytest

from compiler.compiler import (
    BUILTIN_DATATYPES,
    Compiler,
)
from compiler.types import ClassArgument, ClassDefinition, FunctionDefinition


@pytest.fixture
def compiler():
    return Compiler()


def test_process_argument_type_builtins(compiler: Compiler):
    imported_classes = set()
    builtin_types = BUILTIN_DATATYPES.keys()
    for tl_type in builtin_types:
        assert (
            compiler._process_argument_type(tl_type, imported_classes)
            == BUILTIN_DATATYPES[tl_type]
        )
        assert not imported_classes


def test_process_argument_type_vector(compiler: Compiler):
    imported_classes = set()
    arg_type = "vector<int32>"
    assert compiler._process_argument_type(arg_type, imported_classes) == "list[int]"
    assert not imported_classes


def test_process_argument_type_vector_in_vector(compiler: Compiler):
    imported_classes = set()
    arg_type = "vector<vector<int32>>"
    assert (
        compiler._process_argument_type(arg_type, imported_classes) == "list[list[int]]"
    )
    assert not imported_classes


def test_process_argument_type_import(compiler: Compiler):
    imported_classes = set()
    arg_type = "UnknownClass"
    assert (
        compiler._process_argument_type(arg_type, imported_classes)
        == "UnknownClass | None"
    )
    assert imported_classes == {"UnknownClass"}


def test_process_argument_type__vector_import(compiler: Compiler):
    imported_classes = set()
    arg_type = "vector<UnknownClass>"
    assert (
        compiler._process_argument_type(arg_type, imported_classes)
        == "List[UnknownClass]"
    )
    assert imported_classes == {"UnknownClass"}


def test_prepare_arguments(compiler: Compiler):
    arguments = [
        ClassArgument("id", "", "int32"),
        ClassArgument("name", "", "string"),
        ClassArgument("lst", "", "vector<int32>"),
        ClassArgument("imported_class", "", "UnknownClass"),
        ClassArgument("list", "", "vector<int32>"),
    ]
    args_result, imported_classes = compiler.prepare_arguments(arguments)
    assert args_result == [
        'id_: int = Field(default=0, alias="id")',
        'name: str = ""',
        "lst: List[int] = []",
        "imported_class: UnknownClass | None = None",
        'list_: List[int] = Field(default=[], alias="list")',
    ]
    assert imported_classes == {"UnknownClass"}


def test_prepare_docs_class(compiler: Compiler):
    data = ClassDefinition(
        "",
        "Some description",
        arguments=[ClassArgument("id", "user id", "")],
        parent=None,
    )

    assert compiler.prepare_docs(data) == [
        '"""',
        "Some description",
        "",
        ":param id: user id",
        '"""',
    ]


def test_prepare_docs_function(compiler: Compiler):
    data = FunctionDefinition(
        "",
        "Some description",
        arguments=[ClassArgument("id", "user id", "")],
        return_type="Ok",
    )

    assert compiler.prepare_docs(data) == [
        '"""',
        "Some description",
        "",
        ":param id: user id",
        ":return: :class:`Ok`",
        '"""',
    ]


# If found, identifier of the chat to which the link points, 0 otherwise
# Pass true to keep information about downloaded and uploaded files between application restarts
#
