from .function import Function

from .ok import Ok

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class EndGroupCallScreenSharing(Function[Ok]):
    """
    Ends screen sharing in a joined group call

    :param group_call_id: Group call identifier
    :return: :class:`Ok`
    """
    __slots__ = ("group_call_id", "_extra", "_client_id", "_type")

    def __init__(self, group_call_id: int = 0):
        self.group_call_id = group_call_id
        self._type = "endGroupCallScreenSharing"