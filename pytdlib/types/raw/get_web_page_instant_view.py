from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class GetWebPageInstantView(Function):
    """
    Returns an instant view version of a web page if available. This is an offline method if only_local is true. Returns a 404 error if the web page has no instant view page

    :param url: The web page URL
    :param only_local: Pass true to get only locally available information without sending network requests
    :return: :class:`WebPageInstantView`
    """
    __slots__ = ("url", "only_local", "_extra", "_client_id", "_type")

    def __init__(self, url = None, only_local = None):
        self.url = url
        self.only_local = only_local
        self._type = "getWebPageInstantView"