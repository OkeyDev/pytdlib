from .sticker_type import StickerType
from .update import Update
from typing import List

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class UpdateInstalledStickerSets(Update):
    """
    The list of installed sticker sets was updated

    :param sticker_type: Type of the affected stickers
    :param sticker_set_ids: The new list of installed ordinary sticker sets
    """
    __slots__ = ("sticker_type", "sticker_set_ids", "_extra", "_client_id", "_type")

    def __init__(self, sticker_type: StickerType | None = None, sticker_set_ids: List[int] | None = None):
        self.sticker_type = sticker_type
        self.sticker_set_ids = sticker_set_ids
        self._type = "updateInstalledStickerSets"