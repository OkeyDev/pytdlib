from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class EditBotMediaPreview(Function):
    """
    Replaces media preview in the list of media previews of a bot. Returns the new preview after edit is completed server-side

    :param bot_user_id: Identifier of the target bot. The bot must be owned and must have the main Web App
    :param language_code: Language code of the media preview to edit
    :param file_id: File identifier of the media to replace
    :param content: Content of the new preview
    :return: :class:`BotMediaPreview`
    """
    __slots__ = ("bot_user_id", "language_code", "file_id", "content", "_extra", "_client_id", "_type")

    def __init__(self, bot_user_id = None, language_code = None, file_id = None, content = None):
        self.bot_user_id = bot_user_id
        self.language_code = language_code
        self.file_id = file_id
        self.content = content
        self._type = "editBotMediaPreview"