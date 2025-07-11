from .authorization_state import AuthorizationState
from .email_address_authentication_code_info import EmailAddressAuthenticationCodeInfo
from .email_address_reset_state import EmailAddressResetState

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class AuthorizationStateWaitEmailCode(AuthorizationState):
    """
    TDLib needs the user's authentication code sent to an email address to authorize. Call checkAuthenticationEmailCode to provide the code

    :param allow_apple_id: True, if authorization through Apple ID is allowed
    :param allow_google_id: True, if authorization through Google ID is allowed
    :param code_info: Information about the sent authentication code
    :param email_address_reset_state: Reset state of the email address; may be null if the email address can't be reset
    """
    __slots__ = ("allow_apple_id", "allow_google_id", "code_info", "email_address_reset_state", "_extra", "_client_id", "_type")

    def __init__(self, allow_apple_id: bool = False, allow_google_id: bool = False, code_info: EmailAddressAuthenticationCodeInfo | None = None, email_address_reset_state: EmailAddressResetState | None = None):
        self.allow_apple_id = allow_apple_id
        self.allow_google_id = allow_google_id
        self.code_info = code_info
        self.email_address_reset_state = email_address_reset_state
        self._type = "authorizationStateWaitEmailCode"