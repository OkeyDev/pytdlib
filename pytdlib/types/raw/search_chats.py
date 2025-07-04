from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class SearchChats(Function):
    """
    Searches for the specified query in the title and username of already known chats. This is an offline method. Returns chats in the order seen in the main chat list

    :param query: Query to search for. If the query is empty, returns up to 50 recently found chats
    :param limit: The maximum number of chats to be returned
    :return: :class:`Chats`
    """
    __slots__ = ("query", "limit", "_extra", "_client_id", "_type")

    def __init__(self, query = None, limit = None):
        self.query = query
        self.limit = limit
        self._type = "searchChats"