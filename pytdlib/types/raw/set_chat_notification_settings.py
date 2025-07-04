from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class SetChatNotificationSettings(Function):
    """
    Changes the notification settings of a chat. Notification settings of a chat with the current user (Saved Messages) can't be changed

    :param chat_id: Chat identifier
    :param notification_settings: New notification settings for the chat. If the chat is muted for more than 366 days, it is considered to be muted forever
    :return: :class:`Ok`
    """
    __slots__ = ("chat_id", "notification_settings", "_extra", "_client_id", "_type")

    def __init__(self, chat_id = None, notification_settings = None):
        self.chat_id = chat_id
        self.notification_settings = notification_settings
        self._type = "setChatNotificationSettings"