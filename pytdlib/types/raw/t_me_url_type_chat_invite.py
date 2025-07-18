from .t_me_url_type import TMeUrlType

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class TMeUrlTypeChatInvite(TMeUrlType):
    """
    A chat invite link

    :param info: Information about the chat invite link
    """
    __slots__ = ("info", "_extra", "_client_id", "_type")

    def __init__(self, info = None):
        self.info = info
        self._type = "tMeUrlTypeChatInvite"