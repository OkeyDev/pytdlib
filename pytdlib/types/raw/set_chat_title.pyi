from .function import Function

from .ok import Ok

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class SetChatTitle(Function[Ok]):
    """
    Changes the chat title. Supported only for basic groups, supergroups and channels. Requires can_change_info member right

    :param chat_id: Chat identifier
    :param title: New title of the chat; 1-128 characters
    :return: :class:`Ok`
    """
    __slots__ = ("chat_id", "title", "_extra", "_client_id", "_type")

    def __init__(self, chat_id: int = 0, title: str = ""):
        self.chat_id = chat_id
        self.title = title
        self._type = "setChatTitle"