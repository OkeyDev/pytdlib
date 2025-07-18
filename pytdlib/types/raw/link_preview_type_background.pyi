from .background_type import BackgroundType
from .document import Document
from .link_preview_type import LinkPreviewType

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class LinkPreviewTypeBackground(LinkPreviewType):
    """
    The link is a link to a background. Link preview title and description are available only for filled backgrounds

    :param document: Document with the background; may be null for filled backgrounds
    :param background_type: Type of the background; may be null if unknown
    """
    __slots__ = ("document", "background_type", "_extra", "_client_id", "_type")

    def __init__(self, document: Document | None = None, background_type: BackgroundType | None = None):
        self.document = document
        self.background_type = background_type
        self._type = "linkPreviewTypeBackground"