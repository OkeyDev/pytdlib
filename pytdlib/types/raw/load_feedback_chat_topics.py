from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class LoadFeedbackChatTopics(Function):
    """
    Loads more topics in a feedback group; requires administrator rights in the chat. The loaded topics will be sent through updateFeedbackChatTopic. Topics are sorted by their topic.order in descending order. Returns a 404 error if all topics have been loaded

    :param chat_id: Chat identifier of the feedback group
    :param limit: The maximum number of topics to be loaded. For optimal performance, the number of loaded topics is chosen by TDLib and can be smaller than the specified limit, even if the end of the list is not reached
    :return: :class:`Ok`
    """
    __slots__ = ("chat_id", "limit", "_extra", "_client_id", "_type")

    def __init__(self, chat_id = None, limit = None):
        self.chat_id = chat_id
        self.limit = limit
        self._type = "loadFeedbackChatTopics"