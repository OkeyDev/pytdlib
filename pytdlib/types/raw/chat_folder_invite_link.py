from .object_base import ObjectBase

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class ChatFolderInviteLink(ObjectBase):
    """
    Contains a chat folder invite link

    :param invite_link: The chat folder invite link
    :param name: Name of the link
    :param chat_ids: Identifiers of chats, included in the link
    """
    __slots__ = ("invite_link", "name", "chat_ids", "_extra", "_client_id", "_type")

    def __init__(self, invite_link = None, name = None, chat_ids = None):
        self.invite_link = invite_link
        self.name = name
        self.chat_ids = chat_ids
        self._type = "chatFolderInviteLink"