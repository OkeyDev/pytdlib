from .function import Function

from .ok import Ok
from .reaction_type import ReactionType

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class AddMessageReaction(Function[Ok]):
    """
    Adds a reaction or a tag to a message. Use getMessageAvailableReactions to receive the list of available reactions for the message

    :param chat_id: Identifier of the chat to which the message belongs
    :param message_id: Identifier of the message
    :param reaction_type: Type of the reaction to add. Use addPendingPaidMessageReaction instead to add the paid reaction
    :param is_big: Pass true if the reaction is added with a big animation
    :param update_recent_reactions: Pass true if the reaction needs to be added to recent reactions; tags are never added to the list of recent reactions
    :return: :class:`Ok`
    """
    __slots__ = ("chat_id", "message_id", "reaction_type", "is_big", "update_recent_reactions", "_extra", "_client_id", "_type")

    def __init__(self, chat_id: int = 0, message_id: int = 0, reaction_type: ReactionType | None = None, is_big: bool = False, update_recent_reactions: bool = False):
        self.chat_id = chat_id
        self.message_id = message_id
        self.reaction_type = reaction_type
        self.is_big = is_big
        self.update_recent_reactions = update_recent_reactions
        self._type = "addMessageReaction"