from .function import Function

from .stickers import Stickers

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class GetCustomEmojiReactionAnimations(Function[Stickers]):
    """
    Returns TGS stickers with generic animations for custom emoji reactions

    :return: :class:`Stickers`
    """
    __slots__ = ("_extra", "_client_id", "_type")

    def __init__(self):

        self._type = "getCustomEmojiReactionAnimations"