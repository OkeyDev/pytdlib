from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class DeleteDirectMessagesChatTopicHistory(Function):
    """
    Deletes all messages in the topic in a channel direct messages chat administered by the current user

    :param chat_id: Chat identifier of the channel direct messages chat
    :param topic_id: Identifier of the topic which messages will be deleted
    :return: :class:`Ok`
    """
    __slots__ = ("chat_id", "topic_id", "_extra", "_client_id", "_type")

    def __init__(self, chat_id = None, topic_id = None):
        self.chat_id = chat_id
        self.topic_id = topic_id
        self._type = "deleteDirectMessagesChatTopicHistory"