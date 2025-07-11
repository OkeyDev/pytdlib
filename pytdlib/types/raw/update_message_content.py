from .update import Update

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class UpdateMessageContent(Update):
    """
    The message content has changed

    :param chat_id: Chat identifier
    :param message_id: Message identifier
    :param new_content: New message content
    """
    __slots__ = ("chat_id", "message_id", "new_content", "_extra", "_client_id", "_type")

    def __init__(self, chat_id = None, message_id = None, new_content = None):
        self.chat_id = chat_id
        self.message_id = message_id
        self.new_content = new_content
        self._type = "updateMessageContent"