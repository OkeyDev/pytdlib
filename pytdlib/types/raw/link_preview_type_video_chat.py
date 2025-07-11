from .link_preview_type import LinkPreviewType

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class LinkPreviewTypeVideoChat(LinkPreviewType):
    """
    The link is a link to a video chat

    :param photo: Photo of the chat with the video chat; may be null if none
    :param is_live_stream: True, if the video chat is expected to be a live stream in a channel or a broadcast group
    """
    __slots__ = ("photo", "is_live_stream", "_extra", "_client_id", "_type")

    def __init__(self, photo = None, is_live_stream = None):
        self.photo = photo
        self.is_live_stream = is_live_stream
        self._type = "linkPreviewTypeVideoChat"