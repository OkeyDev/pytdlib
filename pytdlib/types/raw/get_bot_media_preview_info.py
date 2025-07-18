from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class GetBotMediaPreviewInfo(Function):
    """
    Returns the list of media previews for the given language and the list of languages for which the bot has dedicated previews

    :param bot_user_id: Identifier of the target bot. The bot must be owned and must have the main Web App
    :param language_code: A two-letter ISO 639-1 language code for which to get previews. If empty, then default previews are returned
    :return: :class:`BotMediaPreviewInfo`
    """
    __slots__ = ("bot_user_id", "language_code", "_extra", "_client_id", "_type")

    def __init__(self, bot_user_id = None, language_code = None):
        self.bot_user_id = bot_user_id
        self.language_code = language_code
        self._type = "getBotMediaPreviewInfo"