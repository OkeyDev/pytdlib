from .function import Function

from .failed_to_add_members import FailedToAddMembers
from typing import List

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class AddChatMembers(Function[FailedToAddMembers]):
    """
    Adds multiple new members to a chat; requires can_invite_users member right. Currently, this method is only available for supergroups and channels. This method can't be used to join a chat. Members can't be added to a channel if it has more than 200 members. Returns information about members that weren't added

    :param chat_id: Chat identifier
    :param user_ids: Identifiers of the users to be added to the chat. The maximum number of added users is 20 for supergroups and 100 for channels
    :return: :class:`FailedToAddMembers`
    """
    __slots__ = ("chat_id", "user_ids", "_extra", "_client_id", "_type")

    def __init__(self, chat_id: int = 0, user_ids: List[int] | None = None):
        self.chat_id = chat_id
        self.user_ids = user_ids
        self._type = "addChatMembers"