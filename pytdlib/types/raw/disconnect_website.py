from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class DisconnectWebsite(Function):
    """
    Disconnects website from the current user's Telegram account

    :param website_id: Website identifier
    :return: :class:`Ok`
    """
    __slots__ = ("website_id", "_extra", "_client_id", "_type")

    def __init__(self, website_id = None):
        self.website_id = website_id
        self._type = "disconnectWebsite"