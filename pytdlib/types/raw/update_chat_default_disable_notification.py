from .update import Update

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class UpdateChatDefaultDisableNotification(Update):
    """
    The value of the default disable_notification parameter, used when a message is sent to the chat, was changed

    :param chat_id: Chat identifier
    :param default_disable_notification: The new default_disable_notification value
    """
    __slots__ = ("chat_id", "default_disable_notification", "_extra", "_client_id", "_type")

    def __init__(self, chat_id = None, default_disable_notification = None):
        self.chat_id = chat_id
        self.default_disable_notification = default_disable_notification
        self._type = "updateChatDefaultDisableNotification"