from .update import Update

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class UpdateChatMessageAutoDeleteTime(Update):
    """
    The message auto-delete or self-destruct timer setting for a chat was changed

    :param chat_id: Chat identifier
    :param message_auto_delete_time: New value of message_auto_delete_time
    """
    __slots__ = ("chat_id", "message_auto_delete_time", "_extra", "_client_id", "_type")

    def __init__(self, chat_id = None, message_auto_delete_time = None):
        self.chat_id = chat_id
        self.message_auto_delete_time = message_auto_delete_time
        self._type = "updateChatMessageAutoDeleteTime"