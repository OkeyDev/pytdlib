from .tl_object import TlObject

class ObjectBase(TlObject):
    __slots__ = ("_extra", "_client_id")