from .internal_link_type import InternalLinkType

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class InternalLinkTypeMainWebApp(InternalLinkType):
    """
    The link is a link to the main Web App of a bot. Call searchPublicChat with the given bot username, check that the user is a bot and has the main Web App. If the bot can be added to attachment menu, then use getAttachmentMenuBot to receive information about the bot, then if the bot isn't added to side menu, show a disclaimer about Mini Apps being third-party applications, ask the user to accept their Terms of service and confirm adding the bot to side and attachment menu, then if the user accepts the terms and confirms adding, use toggleBotIsAddedToAttachmentMenu to add the bot. Then, use getMainWebApp with the given start parameter and mode and open the returned URL as a Web App

    :param bot_username: Username of the bot
    :param start_parameter: Start parameter to be passed to getMainWebApp
    :param mode: The mode to be passed to getMainWebApp
    """
    __slots__ = ("bot_username", "start_parameter", "mode", "_extra", "_client_id", "_type")

    def __init__(self, bot_username = None, start_parameter = None, mode = None):
        self.bot_username = bot_username
        self.start_parameter = start_parameter
        self.mode = mode
        self._type = "internalLinkTypeMainWebApp"