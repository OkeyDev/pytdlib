from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class DeleteQuickReplyShortcutMessages(Function):
    """
    Deletes specified quick reply messages

    :param shortcut_id: Unique identifier of the quick reply shortcut to which the messages belong
    :param message_ids: Unique identifiers of the messages
    :return: :class:`Ok`
    """
    __slots__ = ("shortcut_id", "message_ids", "_extra", "_client_id", "_type")

    def __init__(self, shortcut_id = None, message_ids = None):
        self.shortcut_id = shortcut_id
        self.message_ids = message_ids
        self._type = "deleteQuickReplyShortcutMessages"