from .function import Function

from .ok import Ok
from typing import List

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class DeleteMessages(Function[Ok]):
    """
    Deletes messages

    :param chat_id: Chat identifier
    :param message_ids: Identifiers of the messages to be deleted. Use messageProperties.can_be_deleted_only_for_self and messageProperties.can_be_deleted_for_all_users to get suitable messages
    :param revoke: Pass true to delete messages for all chat members. Always true for supergroups, channels and secret chats
    :return: :class:`Ok`
    """
    __slots__ = ("chat_id", "message_ids", "revoke", "_extra", "_client_id", "_type")

    def __init__(self, chat_id: int = 0, message_ids: List[int] | None = None, revoke: bool = False):
        self.chat_id = chat_id
        self.message_ids = message_ids
        self.revoke = revoke
        self._type = "deleteMessages"