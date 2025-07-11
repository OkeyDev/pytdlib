from .invite_group_call_participant_result import InviteGroupCallParticipantResult

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class InviteGroupCallParticipantResultUserWasBanned(InviteGroupCallParticipantResult):
    """
    The user can't be invited because they were banned by the owner of the call and can be invited back only by the owner of the group call

    """
    __slots__ = ("_extra", "_client_id", "_type")

    def __init__(self):

        self._type = "inviteGroupCallParticipantResultUserWasBanned"