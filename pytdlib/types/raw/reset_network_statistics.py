from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class ResetNetworkStatistics(Function):
    """
    Resets all network data usage statistics to zero. Can be called before authorization

    :return: :class:`Ok`
    """
    __slots__ = ("_extra", "_client_id", "_type")

    def __init__(self):

        self._type = "resetNetworkStatistics"