from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class LoadChats(Function):
    """
    Loads more chats from a chat list. The loaded chats and their positions in the chat list will be sent through updates. Chats are sorted by the pair (chat.position.order, chat.id) in descending order. Returns a 404 error if all chats have been loaded

    :param chat_list: The chat list in which to load chats; pass null to load chats from the main chat list
    :param limit: The maximum number of chats to be loaded. For optimal performance, the number of loaded chats is chosen by TDLib and can be smaller than the specified limit, even if the end of the list is not reached
    :return: :class:`Ok`
    """
    __slots__ = ("chat_list", "limit", "_extra", "_client_id", "_type")

    def __init__(self, chat_list = None, limit = None):
        self.chat_list = chat_list
        self.limit = limit
        self._type = "loadChats"