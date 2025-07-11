from .function import Function

from .outline import Outline

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class GetStickerOutline(Function[Outline]):
    """
    Returns outline of a sticker. This is an offline method. Returns a 404 error if the outline isn't known

    :param sticker_file_id: File identifier of the sticker
    :param for_animated_emoji: Pass true to get the outline scaled for animated emoji
    :param for_clicked_animated_emoji_message: Pass true to get the outline scaled for clicked animated emoji message
    :return: :class:`Outline`
    """
    __slots__ = ("sticker_file_id", "for_animated_emoji", "for_clicked_animated_emoji_message", "_extra", "_client_id", "_type")

    def __init__(self, sticker_file_id: int = 0, for_animated_emoji: bool = False, for_clicked_animated_emoji_message: bool = False):
        self.sticker_file_id = sticker_file_id
        self.for_animated_emoji = for_animated_emoji
        self.for_clicked_animated_emoji_message = for_clicked_animated_emoji_message
        self._type = "getStickerOutline"