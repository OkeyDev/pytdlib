from .call_discard_reason import CallDiscardReason

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class CallDiscardReasonMissed(CallDiscardReason):
    """
    The call was ended before the conversation started. It was canceled by the caller or missed by the other party

    """
    __slots__ = ("_extra", "_client_id", "_type")

    def __init__(self):

        self._type = "callDiscardReasonMissed"