from .chat_permissions import ChatPermissions
from .update import Update

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class UpdateChatPermissions(Update):
    """
    Chat permissions were changed

    :param chat_id: Chat identifier
    :param permissions: The new chat permissions
    """
    __slots__ = ("chat_id", "permissions", "_extra", "_client_id", "_type")

    def __init__(self, chat_id: int = 0, permissions: ChatPermissions | None = None):
        self.chat_id = chat_id
        self.permissions = permissions
        self._type = "updateChatPermissions"