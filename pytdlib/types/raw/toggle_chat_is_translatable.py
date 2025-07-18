from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class ToggleChatIsTranslatable(Function):
    """
    Changes the translatable state of a chat

    :param chat_id: Chat identifier
    :param is_translatable: New value of is_translatable
    :return: :class:`Ok`
    """
    __slots__ = ("chat_id", "is_translatable", "_extra", "_client_id", "_type")

    def __init__(self, chat_id = None, is_translatable = None):
        self.chat_id = chat_id
        self.is_translatable = is_translatable
        self._type = "toggleChatIsTranslatable"