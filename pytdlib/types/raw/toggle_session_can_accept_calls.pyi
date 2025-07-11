from .function import Function

from .ok import Ok

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class ToggleSessionCanAcceptCalls(Function[Ok]):
    """
    Toggles whether a session can accept incoming calls

    :param session_id: Session identifier
    :param can_accept_calls: Pass true to allow accepting incoming calls by the session; pass false otherwise
    :return: :class:`Ok`
    """
    __slots__ = ("session_id", "can_accept_calls", "_extra", "_client_id", "_type")

    def __init__(self, session_id: int = 0, can_accept_calls: bool = False):
        self.session_id = session_id
        self.can_accept_calls = can_accept_calls
        self._type = "toggleSessionCanAcceptCalls"