from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class CreateSecretChat(Function):
    """
    Returns an existing chat corresponding to a known secret chat

    :param secret_chat_id: Secret chat identifier
    :return: :class:`Chat`
    """
    __slots__ = ("secret_chat_id", "_extra", "_client_id", "_type")

    def __init__(self, secret_chat_id = None):
        self.secret_chat_id = secret_chat_id
        self._type = "createSecretChat"