from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class DeclineGroupCallInvitation(Function):
    """
    Declines an invitation to an active group call via messageGroupCall. Can be called both by the sender and the receiver of the invitation

    :param chat_id: Identifier of the chat with the message
    :param message_id: Identifier of the message of the type messageGroupCall
    :return: :class:`Ok`
    """
    __slots__ = ("chat_id", "message_id", "_extra", "_client_id", "_type")

    def __init__(self, chat_id = None, message_id = None):
        self.chat_id = chat_id
        self.message_id = message_id
        self._type = "declineGroupCallInvitation"