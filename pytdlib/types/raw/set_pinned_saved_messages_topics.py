from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class SetPinnedSavedMessagesTopics(Function):
    """
    Changes the order of pinned Saved Messages topics

    :param saved_messages_topic_ids: Identifiers of the new pinned Saved Messages topics
    :return: :class:`Ok`
    """
    __slots__ = ("saved_messages_topic_ids", "_extra", "_client_id", "_type")

    def __init__(self, saved_messages_topic_ids = None):
        self.saved_messages_topic_ids = saved_messages_topic_ids
        self._type = "setPinnedSavedMessagesTopics"