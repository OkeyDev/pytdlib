from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class ReaddQuickReplyShortcutMessages(Function):
    """
    Readds quick reply messages which failed to add. Can be called only for messages for which messageSendingStateFailed.can_retry is true and after specified in messageSendingStateFailed.retry_after time passed. If a message is readded, the corresponding failed to send message is deleted. Returns the sent messages in the same order as the message identifiers passed in message_ids. If a message can't be readded, null will be returned instead of the message

    :param shortcut_name: Name of the target shortcut
    :param message_ids: Identifiers of the quick reply messages to readd. Message identifiers must be in a strictly increasing order
    :return: :class:`QuickReplyMessages`
    """
    __slots__ = ("shortcut_name", "message_ids", "_extra", "_client_id", "_type")

    def __init__(self, shortcut_name = None, message_ids = None):
        self.shortcut_name = shortcut_name
        self.message_ids = message_ids
        self._type = "readdQuickReplyShortcutMessages"