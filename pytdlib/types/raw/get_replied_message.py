from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class GetRepliedMessage(Function):
    """
    Returns information about a non-bundled message that is replied by a given message. Also, returns the pinned message, the game message, the invoice message, the message with a previously set same background, the giveaway message, and the topic creation message for messages of the types messagePinMessage, messageGameScore, messagePaymentSuccessful, messageChatSetBackground, messageGiveawayCompleted and topic messages without non-bundled replied message respectively. Returns a 404 error if the message doesn't exist

    :param chat_id: Identifier of the chat the message belongs to
    :param message_id: Identifier of the reply message
    :return: :class:`Message`
    """
    __slots__ = ("chat_id", "message_id", "_extra", "_client_id", "_type")

    def __init__(self, chat_id = None, message_id = None):
        self.chat_id = chat_id
        self.message_id = message_id
        self._type = "getRepliedMessage"