from .update import Update

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class UpdateQuickReplyShortcutMessages(Update):
    """
    The list of quick reply shortcut messages has changed

    :param shortcut_id: The identifier of the shortcut
    :param messages: The new list of quick reply messages for the shortcut in order from the first to the last sent
    """
    __slots__ = ("shortcut_id", "messages", "_extra", "_client_id", "_type")

    def __init__(self, shortcut_id = None, messages = None):
        self.shortcut_id = shortcut_id
        self.messages = messages
        self._type = "updateQuickReplyShortcutMessages"