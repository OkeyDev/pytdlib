from .supergroup_members_filter import SupergroupMembersFilter

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class SupergroupMembersFilterAdministrators(SupergroupMembersFilter):
    """
    Returns the owner and administrators

    """
    __slots__ = ("_extra", "_client_id", "_type")

    def __init__(self):

        self._type = "supergroupMembersFilterAdministrators"