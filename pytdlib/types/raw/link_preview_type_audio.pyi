from .audio import Audio
from .link_preview_type import LinkPreviewType

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class LinkPreviewTypeAudio(LinkPreviewType):
    """
    The link is a link to an audio

    :param audio: The audio description
    """
    __slots__ = ("audio", "_extra", "_client_id", "_type")

    def __init__(self, audio: Audio | None = None):
        self.audio = audio
        self._type = "linkPreviewTypeAudio"