from .update import Update

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class UpdateTrendingStickerSets(Update):
    """
    The list of trending sticker sets was updated or some of them were viewed

    :param sticker_type: Type of the affected stickers
    :param sticker_sets: The prefix of the list of trending sticker sets with the newest trending sticker sets
    """
    __slots__ = ("sticker_type", "sticker_sets", "_extra", "_client_id", "_type")

    def __init__(self, sticker_type = None, sticker_sets = None):
        self.sticker_type = sticker_type
        self.sticker_sets = sticker_sets
        self._type = "updateTrendingStickerSets"