from .call_discard_reason import CallDiscardReason

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class CallDiscardReasonUpgradeToGroupCall(CallDiscardReason):
    """
    The call was ended because it has been upgraded to a group call

    :param invite_link: Invite link for the group call
    """
    __slots__ = ("invite_link", "_extra", "_client_id", "_type")

    def __init__(self, invite_link = None):
        self.invite_link = invite_link
        self._type = "callDiscardReasonUpgradeToGroupCall"