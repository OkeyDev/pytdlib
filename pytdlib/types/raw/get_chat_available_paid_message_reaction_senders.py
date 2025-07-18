from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class GetChatAvailablePaidMessageReactionSenders(Function):
    """
    Returns the list of message sender identifiers, which can be used to send a paid reaction in a chat

    :param chat_id: Chat identifier
    :return: :class:`MessageSenders`
    """
    __slots__ = ("chat_id", "_extra", "_client_id", "_type")

    def __init__(self, chat_id = None):
        self.chat_id = chat_id
        self._type = "getChatAvailablePaidMessageReactionSenders"