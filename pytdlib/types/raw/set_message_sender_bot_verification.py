from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class SetMessageSenderBotVerification(Function):
    """
    Changes the verification status of a user or a chat by an owned bot

    :param bot_user_id: Identifier of the owned bot, which will verify the user or the chat
    :param verified_id: Identifier of the user or the supergroup or channel chat, which will be verified by the bot
    :param custom_description: Custom description of verification reason; 0-getOption("bot_verification_custom_description_length_max"). If empty, then "was verified by organization "organization_name"" will be used as description. Can be specified only if the bot is allowed to provide custom description
    :return: :class:`Ok`
    """
    __slots__ = ("bot_user_id", "verified_id", "custom_description", "_extra", "_client_id", "_type")

    def __init__(self, bot_user_id = None, verified_id = None, custom_description = None):
        self.bot_user_id = bot_user_id
        self.verified_id = verified_id
        self.custom_description = custom_description
        self._type = "setMessageSenderBotVerification"