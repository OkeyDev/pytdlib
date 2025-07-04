from .function import Function

from .input_chat_photo import InputChatPhoto
from .ok import Ok

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class SetUserPersonalProfilePhoto(Function[Ok]):
    """
    Changes a personal profile photo of a contact user

    :param user_id: User identifier
    :param photo: Profile photo to set; pass null to delete the photo; inputChatPhotoPrevious isn't supported in this function
    :return: :class:`Ok`
    """
    __slots__ = ("user_id", "photo", "_extra", "_client_id", "_type")

    def __init__(self, user_id: int = 0, photo: InputChatPhoto | None = None):
        self.user_id = user_id
        self.photo = photo
        self._type = "setUserPersonalProfilePhoto"