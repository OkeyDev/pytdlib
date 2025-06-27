from dataclasses import dataclass


@dataclass
class ClassArgument:
    name: str
    description: str | None
    type_: str


@dataclass
class BaseObject:
    class_name: str
    description: str | None
    arguments: list[ClassArgument]


@dataclass
class ClassDefinition(BaseObject):
    parent: str | None


@dataclass
class FunctionDefinition(BaseObject):
    return_type: str
