from .function import Function

from .ok import Ok

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class ReadAllChatMentions(Function[Ok]):
    """
    Marks all mentions in a chat as read

    :param chat_id: Chat identifier
    :return: :class:`Ok`
    """
    __slots__ = ("chat_id", "_extra", "_client_id", "_type")

    def __init__(self, chat_id: int = 0):
        self.chat_id = chat_id
        self._type = "readAllChatMentions"