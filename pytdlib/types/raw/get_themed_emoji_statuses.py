from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class GetThemedEmojiStatuses(Function):
    """
    Returns up to 8 emoji statuses, which must be shown right after the default Premium Badge in the emoji status list for self status

    :return: :class:`EmojiStatusCustomEmojis`
    """
    __slots__ = ("_extra", "_client_id", "_type")

    def __init__(self):

        self._type = "getThemedEmojiStatuses"