from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class ReorderBotMediaPreviews(Function):
    """
    Changes order of media previews in the list of media previews of a bot

    :param bot_user_id: Identifier of the target bot. The bot must be owned and must have the main Web App
    :param language_code: Language code of the media previews to reorder
    :param file_ids: File identifiers of the media in the new order
    :return: :class:`Ok`
    """
    __slots__ = ("bot_user_id", "language_code", "file_ids", "_extra", "_client_id", "_type")

    def __init__(self, bot_user_id = None, language_code = None, file_ids = None):
        self.bot_user_id = bot_user_id
        self.language_code = language_code
        self.file_ids = file_ids
        self._type = "reorderBotMediaPreviews"