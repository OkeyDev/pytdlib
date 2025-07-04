from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class EditChatSubscriptionInviteLink(Function):
    """
    Edits a subscription invite link for a channel chat. Requires can_invite_users right in the chat for own links and owner privileges for other links

    :param chat_id: Chat identifier
    :param invite_link: Invite link to be edited
    :param name: Invite link name; 0-32 characters
    :return: :class:`ChatInviteLink`
    """
    __slots__ = ("chat_id", "invite_link", "name", "_extra", "_client_id", "_type")

    def __init__(self, chat_id = None, invite_link = None, name = None):
        self.chat_id = chat_id
        self.invite_link = invite_link
        self.name = name
        self._type = "editChatSubscriptionInviteLink"