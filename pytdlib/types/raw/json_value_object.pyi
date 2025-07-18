from .json_object_member import JsonObjectMember
from .json_value import JsonValue
from typing import List

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class JsonValueObject(JsonValue):
    """
    Represents a JSON object

    :param members: The list of object members
    """
    __slots__ = ("members", "_extra", "_client_id", "_type")

    def __init__(self, members: List[JsonObjectMember] | None = None):
        self.members = members
        self._type = "jsonValueObject"