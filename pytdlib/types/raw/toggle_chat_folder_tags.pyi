from .function import Function

from .ok import Ok

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class ToggleChatFolderTags(Function[Ok]):
    """
    Toggles whether chat folder tags are enabled

    :param are_tags_enabled: Pass true to enable folder tags; pass false to disable them
    :return: :class:`Ok`
    """
    __slots__ = ("are_tags_enabled", "_extra", "_client_id", "_type")

    def __init__(self, are_tags_enabled: bool = False):
        self.are_tags_enabled = are_tags_enabled
        self._type = "toggleChatFolderTags"