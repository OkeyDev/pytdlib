from .function import Function

from .ok import Ok

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class DeleteStickerSet(Function[Ok]):
    """
    Completely deletes a sticker set

    :param name: Sticker set name. The sticker set must be owned by the current user
    :return: :class:`Ok`
    """
    __slots__ = ("name", "_extra", "_client_id", "_type")

    def __init__(self, name: str = ""):
        self.name = name
        self._type = "deleteStickerSet"