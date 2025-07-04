from .object_base import ObjectBase

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class ChatEvents(ObjectBase):
    """
    Contains a list of chat events

    :param events: List of events
    """
    __slots__ = ("events", "_extra", "_client_id", "_type")

    def __init__(self, events = None):
        self.events = events
        self._type = "chatEvents"