from .link_preview_album_media import LinkPreviewAlbumMedia

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class LinkPreviewAlbumMediaPhoto(LinkPreviewAlbumMedia):
    """
    The media is a photo

    :param photo: Photo description
    """
    __slots__ = ("photo", "_extra", "_client_id", "_type")

    def __init__(self, photo = None):
        self.photo = photo
        self._type = "linkPreviewAlbumMediaPhoto"