from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class GetApplicationDownloadLink(Function):
    """
    Returns the link for downloading official Telegram application to be used when the current user invites friends to Telegram

    :return: :class:`HttpUrl`
    """
    __slots__ = ("_extra", "_client_id", "_type")

    def __init__(self):

        self._type = "getApplicationDownloadLink"