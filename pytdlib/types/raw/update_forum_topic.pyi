from .chat_notification_settings import ChatNotificationSettings
from .update import Update

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class UpdateForumTopic(Update):
    """
    Information about a topic in a forum chat was changed

    :param chat_id: Chat identifier
    :param message_thread_id: Message thread identifier of the topic
    :param is_pinned: True, if the topic is pinned in the topic list
    :param last_read_inbox_message_id: Identifier of the last read incoming message
    :param last_read_outbox_message_id: Identifier of the last read outgoing message
    :param unread_mention_count: Number of unread messages with a mention/reply in the topic
    :param unread_reaction_count: Number of messages with unread reactions in the topic
    :param notification_settings: Notification settings for the topic
    """
    __slots__ = ("chat_id", "message_thread_id", "is_pinned", "last_read_inbox_message_id", "last_read_outbox_message_id", "unread_mention_count", "unread_reaction_count", "notification_settings", "_extra", "_client_id", "_type")

    def __init__(self, chat_id: int = 0, message_thread_id: int = 0, is_pinned: bool = False, last_read_inbox_message_id: int = 0, last_read_outbox_message_id: int = 0, unread_mention_count: int = 0, unread_reaction_count: int = 0, notification_settings: ChatNotificationSettings | None = None):
        self.chat_id = chat_id
        self.message_thread_id = message_thread_id
        self.is_pinned = is_pinned
        self.last_read_inbox_message_id = last_read_inbox_message_id
        self.last_read_outbox_message_id = last_read_outbox_message_id
        self.unread_mention_count = unread_mention_count
        self.unread_reaction_count = unread_reaction_count
        self.notification_settings = notification_settings
        self._type = "updateForumTopic"