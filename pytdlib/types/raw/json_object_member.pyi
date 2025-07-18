from .json_value import JsonValue
from .object_base import ObjectBase

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class JsonObjectMember(ObjectBase):
    """
    Represents one member of a JSON object

    :param key: Member's key
    :param value: Member's value
    """
    __slots__ = ("key", "value", "_extra", "_client_id", "_type")

    def __init__(self, key: str = "", value: JsonValue | None = None):
        self.key = key
        self.value = value
        self._type = "jsonObjectMember"