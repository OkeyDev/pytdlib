from .authorization_state import AuthorizationState

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class AuthorizationStateWaitPassword(AuthorizationState):
    """
    The user has been authorized, but needs to enter a 2-step verification password to start using the application. Call checkAuthenticationPassword to provide the password, or requestAuthenticationPasswordRecovery to recover the password, or deleteAccount to delete the account after a week

    :param password_hint: Hint for the password; may be empty
    :param has_recovery_email_address: True, if a recovery email address has been set up
    :param has_passport_data: True, if some Telegram Passport elements were saved
    :param recovery_email_address_pattern: Pattern of the email address to which the recovery email was sent; empty until a recovery email has been sent
    """
    __slots__ = ("password_hint", "has_recovery_email_address", "has_passport_data", "recovery_email_address_pattern", "_extra", "_client_id", "_type")

    def __init__(self, password_hint = None, has_recovery_email_address = None, has_passport_data = None, recovery_email_address_pattern = None):
        self.password_hint = password_hint
        self.has_recovery_email_address = has_recovery_email_address
        self.has_passport_data = has_passport_data
        self.recovery_email_address_pattern = recovery_email_address_pattern
        self._type = "authorizationStateWaitPassword"