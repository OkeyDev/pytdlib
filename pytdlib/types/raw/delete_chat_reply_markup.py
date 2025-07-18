from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class DeleteChatReplyMarkup(Function):
    """
    Deletes the default reply markup from a chat. Must be called after a one-time keyboard or a replyMarkupForceReply reply markup has been used. An updateChatReplyMarkup update will be sent if the reply markup is changed

    :param chat_id: Chat identifier
    :param message_id: The message identifier of the used keyboard
    :return: :class:`Ok`
    """
    __slots__ = ("chat_id", "message_id", "_extra", "_client_id", "_type")

    def __init__(self, chat_id = None, message_id = None):
        self.chat_id = chat_id
        self.message_id = message_id
        self._type = "deleteChatReplyMarkup"