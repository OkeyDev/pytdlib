from .function import Function

from .ok import Ok

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class SetPersonalChat(Function[Ok]):
    """
    Changes the personal chat of the current user

    :param chat_id: Identifier of the new personal chat; pass 0 to remove the chat. Use getSuitablePersonalChats to get suitable chats
    :return: :class:`Ok`
    """
    __slots__ = ("chat_id", "_extra", "_client_id", "_type")

    def __init__(self, chat_id: int = 0):
        self.chat_id = chat_id
        self._type = "setPersonalChat"