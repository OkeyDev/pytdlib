from .function import Function

from .http_url import HttpUrl

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class GetExternalLink(Function[HttpUrl]):
    """
    Returns an HTTP URL which can be used to automatically authorize the current user on a website after clicking an HTTP link. Use the method getExternalLinkInfo to find whether a prior user confirmation is needed

    :param link: The HTTP link
    :param allow_write_access: Pass true if the current user allowed the bot, returned in getExternalLinkInfo, to send them messages
    :return: :class:`HttpUrl`
    """
    __slots__ = ("link", "allow_write_access", "_extra", "_client_id", "_type")

    def __init__(self, link: str = "", allow_write_access: bool = False):
        self.link = link
        self.allow_write_access = allow_write_access
        self._type = "getExternalLink"