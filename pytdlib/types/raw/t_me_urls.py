from .object_base import ObjectBase

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class TMeUrls(ObjectBase):
    """
    Contains a list of t.me URLs

    :param urls: List of URLs
    """
    __slots__ = ("urls", "_extra", "_client_id", "_type")

    def __init__(self, urls = None):
        self.urls = urls
        self._type = "tMeUrls"