from .internal_link_type import InternalLinkType

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class InternalLinkTypeChatFolderInvite(InternalLinkType):
    """
    The link is an invite link to a chat folder. Call checkChatFolderInviteLink with the given invite link to process the link. If the link is valid and the user wants to join the chat folder, then call addChatFolderByInviteLink

    :param invite_link: Internal representation of the invite link
    """
    __slots__ = ("invite_link", "_extra", "_client_id", "_type")

    def __init__(self, invite_link: str = ""):
        self.invite_link = invite_link
        self._type = "internalLinkTypeChatFolderInvite"