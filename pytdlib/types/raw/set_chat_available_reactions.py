from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class SetChatAvailableReactions(Function):
    """
    Changes reactions, available in a chat. Available for basic groups, supergroups, and channels. Requires can_change_info member right

    :param chat_id: Identifier of the chat
    :param available_reactions: Reactions available in the chat. All explicitly specified emoji reactions must be active. In channel chats up to the chat's boost level custom emoji reactions can be explicitly specified
    :return: :class:`Ok`
    """
    __slots__ = ("chat_id", "available_reactions", "_extra", "_client_id", "_type")

    def __init__(self, chat_id = None, available_reactions = None):
        self.chat_id = chat_id
        self.available_reactions = available_reactions
        self._type = "setChatAvailableReactions"