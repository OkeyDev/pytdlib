from .object_base import ObjectBase

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class WebAppInfo(ObjectBase):
    """
    Contains information about a Web App

    :param launch_id: Unique identifier for the Web App launch
    :param url: A Web App URL to open in a web view
    """
    __slots__ = ("launch_id", "url", "_extra", "_client_id", "_type")

    def __init__(self, launch_id: int = 0, url: str = ""):
        self.launch_id = launch_id
        self.url = url
        self._type = "webAppInfo"