from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class BanChatMember(Function):
    """
    Bans a member in a chat; requires can_restrict_members administrator right. Members can't be banned in private or secret chats. In supergroups and channels, the user will not be able to return to the group on their own using invite links, etc., unless unbanned first

    :param chat_id: Chat identifier
    :param member_id: Member identifier
    :param banned_until_date: Point in time (Unix timestamp) when the user will be unbanned; 0 if never. If the user is banned for more than 366 days or for less than 30 seconds from the current time, the user is considered to be banned forever. Ignored in basic groups and if a chat is banned
    :param revoke_messages: Pass true to delete all messages in the chat for the user that is being removed. Always true for supergroups and channels
    :return: :class:`Ok`
    """
    __slots__ = ("chat_id", "member_id", "banned_until_date", "revoke_messages", "_extra", "_client_id", "_type")

    def __init__(self, chat_id = None, member_id = None, banned_until_date = None, revoke_messages = None):
        self.chat_id = chat_id
        self.member_id = member_id
        self.banned_until_date = banned_until_date
        self.revoke_messages = revoke_messages
        self._type = "banChatMember"