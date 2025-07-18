from .thumbnail_format import ThumbnailFormat

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class ThumbnailFormatTgs(ThumbnailFormat):
    """
    The thumbnail is in TGS format. It will be used only for sticker sets

    """
    __slots__ = ("_extra", "_client_id", "_type")

    def __init__(self):

        self._type = "thumbnailFormatTgs"