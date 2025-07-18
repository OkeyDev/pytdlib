from .function import Function

from .ok import Ok

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class CommitPendingPaidMessageReactions(Function[Ok]):
    """
    Applies all pending paid reactions on a message

    :param chat_id: Identifier of the chat to which the message belongs
    :param message_id: Identifier of the message
    :return: :class:`Ok`
    """
    __slots__ = ("chat_id", "message_id", "_extra", "_client_id", "_type")

    def __init__(self, chat_id: int = 0, message_id: int = 0):
        self.chat_id = chat_id
        self.message_id = message_id
        self._type = "commitPendingPaidMessageReactions"