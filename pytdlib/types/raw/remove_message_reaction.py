from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class RemoveMessageReaction(Function):
    """
    Removes a reaction from a message. A chosen reaction can always be removed

    :param chat_id: Identifier of the chat to which the message belongs
    :param message_id: Identifier of the message
    :param reaction_type: Type of the reaction to remove. The paid reaction can't be removed
    :return: :class:`Ok`
    """
    __slots__ = ("chat_id", "message_id", "reaction_type", "_extra", "_client_id", "_type")

    def __init__(self, chat_id = None, message_id = None, reaction_type = None):
        self.chat_id = chat_id
        self.message_id = message_id
        self.reaction_type = reaction_type
        self._type = "removeMessageReaction"