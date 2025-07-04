from .function import Function

from .login_url_info_open import LoginUrlInfoOpen
from .login_url_info_request_confirmation import LoginUrlInfoRequestConfirmation

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class GetExternalLinkInfo(Function[LoginUrlInfoOpen | LoginUrlInfoRequestConfirmation]):
    """
    Returns information about an action to be done when the current user clicks an external link. Don't use this method for links from secret chats if link preview is disabled in secret chats

    :param link: The link
    :return: :class:`LoginUrlInfoOpen | LoginUrlInfoRequestConfirmation`
    """
    __slots__ = ("link", "_extra", "_client_id", "_type")

    def __init__(self, link: str = ""):
        self.link = link
        self._type = "getExternalLinkInfo"