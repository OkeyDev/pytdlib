from .call_state import CallState

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class CallStateHangingUp(CallState):
    """
    The call is hanging up after discardCall has been called

    """
    __slots__ = ("_extra", "_client_id", "_type")

    def __init__(self):

        self._type = "callStateHangingUp"