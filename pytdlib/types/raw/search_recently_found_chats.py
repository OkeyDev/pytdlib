from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class SearchRecentlyFoundChats(Function):
    """
    Searches for the specified query in the title and username of up to 50 recently found chats. This is an offline method

    :param query: Query to search for
    :param limit: The maximum number of chats to be returned
    :return: :class:`Chats`
    """
    __slots__ = ("query", "limit", "_extra", "_client_id", "_type")

    def __init__(self, query = None, limit = None):
        self.query = query
        self.limit = limit
        self._type = "searchRecentlyFoundChats"