from .function import Function

from .input_chat_photo import InputChatPhoto
from .ok import Ok

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class SetProfilePhoto(Function[Ok]):
    """
    Changes a profile photo for the current user

    :param photo: Profile photo to set
    :param is_public: Pass true to set the public photo, which will be visible even the main photo is hidden by privacy settings
    :return: :class:`Ok`
    """
    __slots__ = ("photo", "is_public", "_extra", "_client_id", "_type")

    def __init__(self, photo: InputChatPhoto | None = None, is_public: bool = False):
        self.photo = photo
        self.is_public = is_public
        self._type = "setProfilePhoto"