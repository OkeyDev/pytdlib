from .link_preview_type import LinkPreviewType

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class LinkPreviewTypeAnimation(LinkPreviewType):
    """
    The link is a link to an animation

    :param animation: The animation
    """
    __slots__ = ("animation", "_extra", "_client_id", "_type")

    def __init__(self, animation = None):
        self.animation = animation
        self._type = "linkPreviewTypeAnimation"