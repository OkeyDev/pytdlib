from .function import Function

from .chats import Chats
from .top_chat_category import TopChatCategory

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class GetTopChats(Function[Chats]):
    """
    Returns a list of frequently used chats

    :param category: Category of chats to be returned
    :param limit: The maximum number of chats to be returned; up to 30
    :return: :class:`Chats`
    """
    __slots__ = ("category", "limit", "_extra", "_client_id", "_type")

    def __init__(self, category: TopChatCategory | None = None, limit: int = 0):
        self.category = category
        self.limit = limit
        self._type = "getTopChats"