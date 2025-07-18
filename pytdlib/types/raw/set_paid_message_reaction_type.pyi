from .function import Function

from .ok import Ok
from .paid_reaction_type import PaidReactionType

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class SetPaidMessageReactionType(Function[Ok]):
    """
    Changes type of paid message reaction of the current user on a message. The message must have paid reaction added by the current user

    :param chat_id: Identifier of the chat to which the message belongs
    :param message_id: Identifier of the message
    :param type: New type of the paid reaction
    :return: :class:`Ok`
    """
    __slots__ = ("chat_id", "message_id", "type", "_extra", "_client_id", "_type")

    def __init__(self, chat_id: int = 0, message_id: int = 0, type: PaidReactionType | None = None):
        self.chat_id = chat_id
        self.message_id = message_id
        self.type = type
        self._type = "setPaidMessageReactionType"