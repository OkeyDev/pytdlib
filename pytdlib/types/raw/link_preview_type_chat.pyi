from .chat_photo import ChatPhoto
from .invite_link_chat_type import InviteLinkChatType
from .link_preview_type import LinkPreviewType

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class LinkPreviewTypeChat(LinkPreviewType):
    """
    The link is a link to a chat

    :param type: Type of the chat
    :param photo: Photo of the chat; may be null
    :param creates_join_request: True, if the link only creates join request
    """
    __slots__ = ("type", "photo", "creates_join_request", "_extra", "_client_id", "_type")

    def __init__(self, type: InviteLinkChatType | None = None, photo: ChatPhoto | None = None, creates_join_request: bool = False):
        self.type = type
        self.photo = photo
        self.creates_join_request = creates_join_request
        self._type = "linkPreviewTypeChat"