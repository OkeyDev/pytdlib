import typing
from .tl_object import TlObject

T = typing.TypeVar("T")


class Function(TlObject, typing.Generic[T]):
    __slots__ = ("_extra", "_client_id")