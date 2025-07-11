from .function import Function

from .found_messages import FoundMessages
from .search_messages_filter import SearchMessagesFilter

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class SearchSecretMessages(Function[FoundMessages]):
    """
    Searches for messages in secret chats. Returns the results in reverse chronological order. For optimal performance, the number of returned messages is chosen by TDLib

    :param chat_id: Identifier of the chat in which to search. Specify 0 to search in all secret chats
    :param query: Query to search for. If empty, searchChatMessages must be used instead
    :param offset: Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results
    :param limit: The maximum number of messages to be returned; up to 100. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit
    :param filter: Additional filter for messages to search; pass null to search for all messages
    :return: :class:`FoundMessages`
    """
    __slots__ = ("chat_id", "query", "offset", "limit", "filter", "_extra", "_client_id", "_type")

    def __init__(self, chat_id: int = 0, query: str = "", offset: str = "", limit: int = 0, filter: SearchMessagesFilter | None = None):
        self.chat_id = chat_id
        self.query = query
        self.offset = offset
        self.limit = limit
        self.filter = filter
        self._type = "searchSecretMessages"