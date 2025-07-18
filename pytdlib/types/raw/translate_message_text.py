from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class TranslateMessageText(Function):
    """
    Extracts text or caption of the given message and translates it to the given language. If the current user is a Telegram Premium user, then text formatting is preserved

    :param chat_id: Identifier of the chat to which the message belongs
    :param message_id: Identifier of the message
    :param to_language_code: Language code of the language to which the message is translated. Must be one of "af", "sq", "am", "ar", "hy", "az", "eu", "be", "bn", "bs", "bg", "ca", "ceb", "zh-CN", "zh", "zh-Hans", "zh-TW", "zh-Hant", "co", "hr", "cs", "da", "nl", "en", "eo", "et", "fi", "fr", "fy", "gl", "ka", "de", "el", "gu", "ht", "ha", "haw", "he", "iw", "hi", "hmn", "hu", "is", "ig", "id", "in", "ga", "it", "ja", "jv", "kn", "kk", "km", "rw", "ko", "ku", "ky", "lo", "la", "lv", "lt", "lb", "mk", "mg", "ms", "ml", "mt", "mi", "mr", "mn", "my", "ne", "no", "ny", "or", "ps", "fa", "pl", "pt", "pa", "ro", "ru", "sm", "gd", "sr", "st", "sn", "sd", "si", "sk", "sl", "so", "es", "su", "sw", "sv", "tl", "tg", "ta", "tt", "te", "th", "tr", "tk", "uk", "ur", "ug", "uz", "vi", "cy", "xh", "yi", "ji", "yo", "zu"
    :return: :class:`FormattedText`
    """
    __slots__ = ("chat_id", "message_id", "to_language_code", "_extra", "_client_id", "_type")

    def __init__(self, chat_id = None, message_id = None, to_language_code = None):
        self.chat_id = chat_id
        self.message_id = message_id
        self.to_language_code = to_language_code
        self._type = "translateMessageText"