from .function import Function

from .ok import Ok

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class SetBusinessMessageIsPinned(Function[Ok]):
    """
    Pins or unpins a message sent on behalf of a business account; for bots only

    :param business_connection_id: Unique identifier of business connection on behalf of which the message was sent
    :param chat_id: The chat the message belongs to
    :param message_id: Identifier of the message
    :param is_pinned: Pass true to pin the message, pass false to unpin it
    :return: :class:`Ok`
    """
    __slots__ = ("business_connection_id", "chat_id", "message_id", "is_pinned", "_extra", "_client_id", "_type")

    def __init__(self, business_connection_id: str = "", chat_id: int = 0, message_id: int = 0, is_pinned: bool = False):
        self.business_connection_id = business_connection_id
        self.chat_id = chat_id
        self.message_id = message_id
        self.is_pinned = is_pinned
        self._type = "setBusinessMessageIsPinned"