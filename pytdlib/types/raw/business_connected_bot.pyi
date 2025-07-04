from .business_bot_rights import BusinessBotRights
from .business_recipients import BusinessRecipients
from .object_base import ObjectBase

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class BusinessConnectedBot(ObjectBase):
    """
    Describes a bot connected to a business account

    :param bot_user_id: User identifier of the bot
    :param recipients: Private chats that will be accessible to the bot
    :param rights: Rights of the bot
    """
    __slots__ = ("bot_user_id", "recipients", "rights", "_extra", "_client_id", "_type")

    def __init__(self, bot_user_id: int = 0, recipients: BusinessRecipients | None = None, rights: BusinessBotRights | None = None):
        self.bot_user_id = bot_user_id
        self.recipients = recipients
        self.rights = rights
        self._type = "businessConnectedBot"