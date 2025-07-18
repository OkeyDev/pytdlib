from .chat_member_status import ChatMemberStatus
from .object_base import ObjectBase

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class BasicGroup(ObjectBase):
    """
    Represents a basic group of 0-200 users (must be upgraded to a supergroup to accommodate more than 200 users)

    :param id: Group identifier
    :param member_count: Number of members in the group
    :param status: Status of the current user in the group
    :param is_active: True, if the group is active
    :param upgraded_to_supergroup_id: Identifier of the supergroup to which this group was upgraded; 0 if none
    """
    __slots__ = ("id", "member_count", "status", "is_active", "upgraded_to_supergroup_id", "_extra", "_client_id", "_type")

    def __init__(self, id: int = 0, member_count: int = 0, status: ChatMemberStatus | None = None, is_active: bool = False, upgraded_to_supergroup_id: int = 0):
        self.id = id
        self.member_count = member_count
        self.status = status
        self.is_active = is_active
        self.upgraded_to_supergroup_id = upgraded_to_supergroup_id
        self._type = "basicGroup"