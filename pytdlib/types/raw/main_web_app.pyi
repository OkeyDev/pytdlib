from .object_base import ObjectBase
from .web_app_open_mode import WebAppOpenMode

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class MainWebApp(ObjectBase):
    """
    Contains information about the main Web App of a bot

    :param url: URL of the Web App to open
    :param mode: The mode in which the Web App must be opened
    """
    __slots__ = ("url", "mode", "_extra", "_client_id", "_type")

    def __init__(self, url: str = "", mode: WebAppOpenMode | None = None):
        self.url = url
        self.mode = mode
        self._type = "mainWebApp"