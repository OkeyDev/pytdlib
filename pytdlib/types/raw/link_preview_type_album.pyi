from .link_preview_album_media import LinkPreviewAlbumMedia
from .link_preview_type import LinkPreviewType
from typing import List

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class LinkPreviewTypeAlbum(LinkPreviewType):
    """
    The link is a link to a media album consisting of photos and videos

    :param media: The list of album media
    :param caption: Album caption
    """
    __slots__ = ("media", "caption", "_extra", "_client_id", "_type")

    def __init__(self, media: List[LinkPreviewAlbumMedia] | None = None, caption: str = ""):
        self.media = media
        self.caption = caption
        self._type = "linkPreviewTypeAlbum"