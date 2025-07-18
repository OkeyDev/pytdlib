from .link_preview_type import LinkPreviewType
from .sticker import Sticker

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class LinkPreviewTypeSticker(LinkPreviewType):
    """
    The link is a link to a sticker

    :param sticker: The sticker. It can be an arbitrary WEBP image and can have dimensions bigger than 512
    """
    __slots__ = ("sticker", "_extra", "_client_id", "_type")

    def __init__(self, sticker: Sticker | None = None):
        self.sticker = sticker
        self._type = "linkPreviewTypeSticker"