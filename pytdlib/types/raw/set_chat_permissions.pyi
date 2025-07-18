from .function import Function

from .chat_permissions import ChatPermissions
from .ok import Ok

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class SetChatPermissions(Function[Ok]):
    """
    Changes the chat members permissions. Supported only for basic groups and supergroups. Requires can_restrict_members administrator right

    :param chat_id: Chat identifier
    :param permissions: New non-administrator members permissions in the chat
    :return: :class:`Ok`
    """
    __slots__ = ("chat_id", "permissions", "_extra", "_client_id", "_type")

    def __init__(self, chat_id: int = 0, permissions: ChatPermissions | None = None):
        self.chat_id = chat_id
        self.permissions = permissions
        self._type = "setChatPermissions"