from .secret_chat_state import SecretChatState

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class SecretChatStateClosed(SecretChatState):
    """
    The secret chat is closed

    """
    __slots__ = ("_extra", "_client_id", "_type")

    def __init__(self):

        self._type = "secretChatStateClosed"