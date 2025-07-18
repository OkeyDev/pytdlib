from .object_base import ObjectBase

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class MessagePosition(ObjectBase):
    """
    Contains information about a message in a specific position

    :param position: 0-based message position in the full list of suitable messages
    :param message_id: Message identifier
    :param date: Point in time (Unix timestamp) when the message was sent
    """
    __slots__ = ("position", "message_id", "date", "_extra", "_client_id", "_type")

    def __init__(self, position: int = 0, message_id: int = 0, date: int = 0):
        self.position = position
        self.message_id = message_id
        self.date = date
        self._type = "messagePosition"