from .call_problem import CallProblem

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class CallProblemSilentRemote(CallProblem):
    """
    The other side couldn't hear the user

    """
    __slots__ = ("_extra", "_client_id", "_type")

    def __init__(self):

        self._type = "callProblemSilentRemote"