from .input_chat_photo import InputChatPhoto

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class InputChatPhotoPrevious(InputChatPhoto):
    """
    A previously used profile photo of the current user

    :param chat_photo_id: Identifier of the current user's profile photo to reuse
    """
    __slots__ = ("chat_photo_id", "_extra", "_client_id", "_type")

    def __init__(self, chat_photo_id: int = 0):
        self.chat_photo_id = chat_photo_id
        self._type = "inputChatPhotoPrevious"