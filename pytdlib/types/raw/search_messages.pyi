from .function import Function

from .chat_list import ChatList
from .found_messages import FoundMessages
from .search_messages_chat_type_filter import SearchMessagesChatTypeFilter
from .search_messages_filter import SearchMessagesFilter

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class SearchMessages(Function[FoundMessages]):
    """
    Searches for messages in all chats except secret chats. Returns the results in reverse chronological order (i.e., in order of decreasing (date, chat_id, message_id)). For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit

    :param chat_list: Chat list in which to search messages; pass null to search in all chats regardless of their chat list. Only Main and Archive chat lists are supported
    :param query: Query to search for
    :param offset: Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results
    :param limit: The maximum number of messages to be returned; up to 100. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit
    :param filter: Additional filter for messages to search; pass null to search for all messages. Filters searchMessagesFilterMention, searchMessagesFilterUnreadMention, searchMessagesFilterUnreadReaction, searchMessagesFilterFailedToSend, and searchMessagesFilterPinned are unsupported in this function
    :param chat_type_filter: Additional filter for type of the chat of the searched messages; pass null to search for messages in all chats
    :param min_date: If not 0, the minimum date of the messages to return
    :param max_date: If not 0, the maximum date of the messages to return
    :return: :class:`FoundMessages`
    """
    __slots__ = ("chat_list", "query", "offset", "limit", "filter", "chat_type_filter", "min_date", "max_date", "_extra", "_client_id", "_type")

    def __init__(self, chat_list: ChatList | None = None, query: str = "", offset: str = "", limit: int = 0, filter: SearchMessagesFilter | None = None, chat_type_filter: SearchMessagesChatTypeFilter | None = None, min_date: int = 0, max_date: int = 0):
        self.chat_list = chat_list
        self.query = query
        self.offset = offset
        self.limit = limit
        self.filter = filter
        self.chat_type_filter = chat_type_filter
        self.min_date = min_date
        self.max_date = max_date
        self._type = "searchMessages"