from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class ReadAllChatReactions(Function):
    """
    Marks all reactions in a chat or a forum topic as read

    :param chat_id: Chat identifier
    :return: :class:`Ok`
    """
    __slots__ = ("chat_id", "_extra", "_client_id", "_type")

    def __init__(self, chat_id = None):
        self.chat_id = chat_id
        self._type = "readAllChatReactions"