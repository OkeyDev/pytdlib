from .chat_list import ChatList
from .update import Update

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class UpdateChatRemovedFromList(Update):
    """
    A chat was removed from a chat list

    :param chat_id: Chat identifier
    :param chat_list: The chat list from which the chat was removed
    """
    __slots__ = ("chat_id", "chat_list", "_extra", "_client_id", "_type")

    def __init__(self, chat_id: int = 0, chat_list: ChatList | None = None):
        self.chat_id = chat_id
        self.chat_list = chat_list
        self._type = "updateChatRemovedFromList"