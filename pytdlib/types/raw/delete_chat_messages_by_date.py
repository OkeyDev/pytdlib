from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class DeleteChatMessagesByDate(Function):
    """
    Deletes all messages between the specified dates in a chat. Supported only for private chats and basic groups. Messages sent in the last 30 seconds will not be deleted

    :param chat_id: Chat identifier
    :param min_date: The minimum date of the messages to delete
    :param max_date: The maximum date of the messages to delete
    :param revoke: Pass true to delete chat messages for all users; private chats only
    :return: :class:`Ok`
    """
    __slots__ = ("chat_id", "min_date", "max_date", "revoke", "_extra", "_client_id", "_type")

    def __init__(self, chat_id = None, min_date = None, max_date = None, revoke = None):
        self.chat_id = chat_id
        self.min_date = min_date
        self.max_date = max_date
        self.revoke = revoke
        self._type = "deleteChatMessagesByDate"