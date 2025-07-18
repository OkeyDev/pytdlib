from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class ResendEmailAddressVerificationCode(Function):
    """
    Resends the code to verify an email address to be added to a user's Telegram Passport

    :return: :class:`EmailAddressAuthenticationCodeInfo`
    """
    __slots__ = ("_extra", "_client_id", "_type")

    def __init__(self):

        self._type = "resendEmailAddressVerificationCode"