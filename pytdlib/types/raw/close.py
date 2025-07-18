from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class Close(Function):
    """
    Closes the TDLib instance. All databases will be flushed to disk and properly closed. After the close completes, updateAuthorizationState with authorizationStateClosed will be sent. Can be called before initialization

    :return: :class:`Ok`
    """
    __slots__ = ("_extra", "_client_id", "_type")

    def __init__(self):

        self._type = "close"