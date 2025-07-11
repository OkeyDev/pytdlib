from .location import Location
from .object_base import ObjectBase

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class ChatLocation(ObjectBase):
    """
    Represents a location to which a chat is connected

    :param location: The location
    :param address: Location address; 1-64 characters, as defined by the chat owner
    """
    __slots__ = ("location", "address", "_extra", "_client_id", "_type")

    def __init__(self, location: Location | None = None, address: str = ""):
        self.location = location
        self.address = address
        self._type = "chatLocation"