from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class CheckLoginEmailAddressCode(Function):
    """
    Checks the login email address authentication

    :param code: Email address authentication to check
    :return: :class:`Ok`
    """
    __slots__ = ("code", "_extra", "_client_id", "_type")

    def __init__(self, code = None):
        self.code = code
        self._type = "checkLoginEmailAddressCode"