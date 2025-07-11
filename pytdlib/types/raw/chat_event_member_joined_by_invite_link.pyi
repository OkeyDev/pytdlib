from .chat_event_action import ChatEventAction
from .chat_invite_link import ChatInviteLink

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class ChatEventMemberJoinedByInviteLink(ChatEventAction):
    """
    A new member joined the chat via an invite link

    :param invite_link: Invite link used to join the chat
    :param via_chat_folder_invite_link: True, if the user has joined the chat using an invite link for a chat folder
    """
    __slots__ = ("invite_link", "via_chat_folder_invite_link", "_extra", "_client_id", "_type")

    def __init__(self, invite_link: ChatInviteLink | None = None, via_chat_folder_invite_link: bool = False):
        self.invite_link = invite_link
        self.via_chat_folder_invite_link = via_chat_folder_invite_link
        self._type = "chatEventMemberJoinedByInviteLink"