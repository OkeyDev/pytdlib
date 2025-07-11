from .secret_chat_state import SecretChatState

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class SecretChatStatePending(SecretChatState):
    """
    The secret chat is not yet created; waiting for the other user to get online

    """
    __slots__ = ("_extra", "_client_id", "_type")

    def __init__(self):

        self._type = "secretChatStatePending"