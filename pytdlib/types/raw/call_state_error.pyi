from .call_state import CallState
from .error import Error

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class CallStateError(CallState):
    """
    The call has ended with an error

    :param error: Error. An error with the code 4005000 will be returned if an outgoing call is missed because of an expired timeout
    """
    __slots__ = ("error", "_extra", "_client_id", "_type")

    def __init__(self, error: Error | None = None):
        self.error = error
        self._type = "callStateError"