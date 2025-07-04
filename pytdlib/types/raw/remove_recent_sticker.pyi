from .function import Function

from .input_file import InputFile
from .ok import Ok

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class RemoveRecentSticker(Function[Ok]):
    """
    Removes a sticker from the list of recently used stickers

    :param is_attached: Pass true to remove the sticker from the list of stickers recently attached to photo or video files; pass false to remove the sticker from the list of recently sent stickers
    :param sticker: Sticker file to delete
    :return: :class:`Ok`
    """
    __slots__ = ("is_attached", "sticker", "_extra", "_client_id", "_type")

    def __init__(self, is_attached: bool = False, sticker: InputFile | None = None):
        self.is_attached = is_attached
        self.sticker = sticker
        self._type = "removeRecentSticker"