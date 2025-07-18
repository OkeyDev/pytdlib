from .object_base import ObjectBase

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class WebApp(ObjectBase):
    """
    Describes a Web App. Use getInternalLink with internalLinkTypeWebApp to share the Web App

    :param short_name: Web App short name
    :param title: Web App title
    :param description: Describes a Web App. Use getInternalLink with internalLinkTypeWebApp to share the Web App
    :param photo: Web App photo
    :param animation: Web App animation; may be null
    """
    __slots__ = ("short_name", "title", "description", "photo", "animation", "_extra", "_client_id", "_type")

    def __init__(self, short_name = None, title = None, description = None, photo = None, animation = None):
        self.short_name = short_name
        self.title = title
        self.description = description
        self.photo = photo
        self.animation = animation
        self._type = "webApp"