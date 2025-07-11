from .function import Function

from .message import Message

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class GetMessageLocally(Function[Message]):
    """
    Returns information about a message, if it is available without sending network request. Returns a 404 error if message isn't available locally. This is an offline method

    :param chat_id: Identifier of the chat the message belongs to
    :param message_id: Identifier of the message to get
    :return: :class:`Message`
    """
    __slots__ = ("chat_id", "message_id", "_extra", "_client_id", "_type")

    def __init__(self, chat_id: int = 0, message_id: int = 0):
        self.chat_id = chat_id
        self.message_id = message_id
        self._type = "getMessageLocally"