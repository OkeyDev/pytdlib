from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class SetStickerSetThumbnail(Function):
    """
    Sets a sticker set thumbnail

    :param user_id: Sticker set owner; ignored for regular users
    :param name: Sticker set name. The sticker set must be owned by the current user
    :param thumbnail: Thumbnail to set; pass null to remove the sticker set thumbnail
    :param format: Format of the thumbnail; pass null if thumbnail is removed
    :return: :class:`Ok`
    """
    __slots__ = ("user_id", "name", "thumbnail", "format", "_extra", "_client_id", "_type")

    def __init__(self, user_id = None, name = None, thumbnail = None, format = None):
        self.user_id = user_id
        self.name = name
        self.thumbnail = thumbnail
        self.format = format
        self._type = "setStickerSetThumbnail"