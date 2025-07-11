from .function import Function

from .ok import Ok

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class DeleteChatFolderInviteLink(Function[Ok]):
    """
    Deletes an invite link for a chat folder

    :param chat_folder_id: Chat folder identifier
    :param invite_link: Invite link to be deleted
    :return: :class:`Ok`
    """
    __slots__ = ("chat_folder_id", "invite_link", "_extra", "_client_id", "_type")

    def __init__(self, chat_folder_id: int = 0, invite_link: str = ""):
        self.chat_folder_id = chat_folder_id
        self.invite_link = invite_link
        self._type = "deleteChatFolderInviteLink"