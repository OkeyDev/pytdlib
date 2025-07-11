from .link_preview_album_media import LinkPreviewAlbumMedia

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class LinkPreviewAlbumMediaVideo(LinkPreviewAlbumMedia):
    """
    The media is a video

    :param video: Video description
    """
    __slots__ = ("video", "_extra", "_client_id", "_type")

    def __init__(self, video = None):
        self.video = video
        self._type = "linkPreviewAlbumMediaVideo"