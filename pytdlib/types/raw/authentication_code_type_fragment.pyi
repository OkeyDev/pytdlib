from .authentication_code_type import AuthenticationCodeType

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class AuthenticationCodeTypeFragment(AuthenticationCodeType):
    """
    A digit-only authentication code is delivered to https://fragment.com. The user must be logged in there via a wallet owning the phone number's NFT

    :param url: URL to open to receive the code
    :param length: Length of the code
    """
    __slots__ = ("url", "length", "_extra", "_client_id", "_type")

    def __init__(self, url: str = "", length: int = 0):
        self.url = url
        self.length = length
        self._type = "authenticationCodeTypeFragment"