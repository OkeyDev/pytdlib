from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class GetChatMessageCount(Function):
    """
    Returns approximate number of messages of the specified type in the chat or its topic

    :param chat_id: Identifier of the chat in which to count messages
    :param topic_id: Pass topic identifier to get number of messages only in specific topic; pass null to get number of messages in all topics
    :param filter: Filter for message content; searchMessagesFilterEmpty is unsupported in this function
    :param return_local: Pass true to get the number of messages without sending network requests, or -1 if the number of messages is unknown locally
    :return: :class:`Count`
    """
    __slots__ = ("chat_id", "topic_id", "filter", "return_local", "_extra", "_client_id", "_type")

    def __init__(self, chat_id = None, topic_id = None, filter = None, return_local = None):
        self.chat_id = chat_id
        self.topic_id = topic_id
        self.filter = filter
        self.return_local = return_local
        self._type = "getChatMessageCount"