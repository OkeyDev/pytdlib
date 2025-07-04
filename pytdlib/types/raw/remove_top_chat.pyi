from .function import Function

from .ok import Ok
from .top_chat_category import TopChatCategory

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class RemoveTopChat(Function[Ok]):
    """
    Removes a chat from the list of frequently used chats. Supported only if the chat info database is enabled

    :param category: Category of frequently used chats
    :param chat_id: Chat identifier
    :return: :class:`Ok`
    """
    __slots__ = ("category", "chat_id", "_extra", "_client_id", "_type")

    def __init__(self, category: TopChatCategory | None = None, chat_id: int = 0):
        self.category = category
        self.chat_id = chat_id
        self._type = "removeTopChat"