from .call_discard_reason import CallDiscardReason

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class CallDiscardReasonEmpty(CallDiscardReason):
    """
    The call wasn't discarded, or the reason is unknown

    """
    __slots__ = ("_extra", "_client_id", "_type")

    def __init__(self):

        self._type = "callDiscardReasonEmpty"