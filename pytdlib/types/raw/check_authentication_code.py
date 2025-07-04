from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class CheckAuthenticationCode(Function):
    """
    Checks the authentication code. Works only when the current authorization state is authorizationStateWaitCode

    :param code: Authentication code to check
    :return: :class:`Ok`
    """
    __slots__ = ("code", "_extra", "_client_id", "_type")

    def __init__(self, code = None):
        self.code = code
        self._type = "checkAuthenticationCode"