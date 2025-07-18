from .function import Function

from .email_address_authentication import EmailAddressAuthentication
from .ok import Ok

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class CheckLoginEmailAddressCode(Function[Ok]):
    """
    Checks the login email address authentication

    :param code: Email address authentication to check
    :return: :class:`Ok`
    """
    __slots__ = ("code", "_extra", "_client_id", "_type")

    def __init__(self, code: EmailAddressAuthentication | None = None):
        self.code = code
        self._type = "checkLoginEmailAddressCode"