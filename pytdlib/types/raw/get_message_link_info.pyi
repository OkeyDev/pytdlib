from .function import Function

from .message_link_info import MessageLinkInfo

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class GetMessageLinkInfo(Function[MessageLinkInfo]):
    """
    Returns information about a public or private message link. Can be called for any internal link of the type internalLinkTypeMessage

    :param url: The message link
    :return: :class:`MessageLinkInfo`
    """
    __slots__ = ("url", "_extra", "_client_id", "_type")

    def __init__(self, url: str = ""):
        self.url = url
        self._type = "getMessageLinkInfo"