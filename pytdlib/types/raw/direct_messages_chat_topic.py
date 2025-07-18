from .object_base import ObjectBase

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class DirectMessagesChatTopic(ObjectBase):
    """
    Contains information about a topic in a channel direct messages chat administered by the current user

    :param chat_id: Identifier of the chat to which the topic belongs
    :param id: Unique topic identifier
    :param sender_id: Identifier of the user or chat that sends the messages to the topic
    :param order: A parameter used to determine order of the topic in the topic list. Topics must be sorted by the order in descending order
    :param is_marked_as_unread: True, if the forum topic is marked as unread
    :param unread_count: Number of unread messages in the chat
    :param last_read_inbox_message_id: Identifier of the last read incoming message
    :param last_read_outbox_message_id: Identifier of the last read outgoing message
    :param unread_reaction_count: Number of messages with unread reactions in the chat
    :param last_message: Last message in the topic; may be null if none or unknown
    :param draft_message: A draft of a message in the topic; may be null if none
    """
    __slots__ = ("chat_id", "id", "sender_id", "order", "is_marked_as_unread", "unread_count", "last_read_inbox_message_id", "last_read_outbox_message_id", "unread_reaction_count", "last_message", "draft_message", "_extra", "_client_id", "_type")

    def __init__(self, chat_id = None, id = None, sender_id = None, order = None, is_marked_as_unread = None, unread_count = None, last_read_inbox_message_id = None, last_read_outbox_message_id = None, unread_reaction_count = None, last_message = None, draft_message = None):
        self.chat_id = chat_id
        self.id = id
        self.sender_id = sender_id
        self.order = order
        self.is_marked_as_unread = is_marked_as_unread
        self.unread_count = unread_count
        self.last_read_inbox_message_id = last_read_inbox_message_id
        self.last_read_outbox_message_id = last_read_outbox_message_id
        self.unread_reaction_count = unread_reaction_count
        self.last_message = last_message
        self.draft_message = draft_message
        self._type = "directMessagesChatTopic"