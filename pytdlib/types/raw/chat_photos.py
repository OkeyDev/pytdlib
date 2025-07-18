from .object_base import ObjectBase

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class ChatPhotos(ObjectBase):
    """
    Contains a list of chat or user profile photos

    :param total_count: Total number of photos
    :param photos: List of photos
    """
    __slots__ = ("total_count", "photos", "_extra", "_client_id", "_type")

    def __init__(self, total_count = None, photos = None):
        self.total_count = total_count
        self.photos = photos
        self._type = "chatPhotos"