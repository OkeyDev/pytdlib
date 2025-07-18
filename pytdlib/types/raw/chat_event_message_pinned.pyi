from .chat_event_action import ChatEventAction
from .message import Message

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class ChatEventMessagePinned(ChatEventAction):
    """
    A message was pinned

    :param message: Pinned message
    """
    __slots__ = ("message", "_extra", "_client_id", "_type")

    def __init__(self, message: Message | None = None):
        self.message = message
        self._type = "chatEventMessagePinned"