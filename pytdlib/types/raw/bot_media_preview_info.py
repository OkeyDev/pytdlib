from .object_base import ObjectBase

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class BotMediaPreviewInfo(ObjectBase):
    """
    Contains a list of media previews of a bot for the given language and the list of languages for which the bot has dedicated previews

    :param previews: List of media previews
    :param language_codes: List of language codes for which the bot has dedicated previews
    """
    __slots__ = ("previews", "language_codes", "_extra", "_client_id", "_type")

    def __init__(self, previews = None, language_codes = None):
        self.previews = previews
        self.language_codes = language_codes
        self._type = "botMediaPreviewInfo"