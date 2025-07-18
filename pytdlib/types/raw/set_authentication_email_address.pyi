from .function import Function

from .ok import Ok

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class SetAuthenticationEmailAddress(Function[Ok]):
    """
    Sets the email address of the user and sends an authentication code to the email address. Works only when the current authorization state is authorizationStateWaitEmailAddress

    :param email_address: The email address of the user
    :return: :class:`Ok`
    """
    __slots__ = ("email_address", "_extra", "_client_id", "_type")

    def __init__(self, email_address: str = ""):
        self.email_address = email_address
        self._type = "setAuthenticationEmailAddress"