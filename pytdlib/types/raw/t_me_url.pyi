from .object_base import ObjectBase
from .t_me_url_type import TMeUrlType

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class TMeUrl(ObjectBase):
    """
    Represents a URL linking to an internal Telegram entity

    :param url: URL
    :param type: Type of the URL
    """
    __slots__ = ("url", "type", "_extra", "_client_id", "_type")

    def __init__(self, url: str = "", type: TMeUrlType | None = None):
        self.url = url
        self.type = type
        self._type = "tMeUrl"