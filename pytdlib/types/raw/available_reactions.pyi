from .available_reaction import AvailableReaction
from .object_base import ObjectBase
from .reaction_unavailability_reason import ReactionUnavailabilityReason
from typing import List

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class AvailableReactions(ObjectBase):
    """
    Represents a list of reactions that can be added to a message

    :param top_reactions: List of reactions to be shown at the top
    :param recent_reactions: List of recently used reactions
    :param popular_reactions: List of popular reactions
    :param allow_custom_emoji: True, if any custom emoji reaction can be added by Telegram Premium subscribers
    :param are_tags: True, if the reactions will be tags and the message can be found by them
    :param unavailability_reason: The reason why the current user can't add reactions to the message, despite some other users can; may be null if none
    """
    __slots__ = ("top_reactions", "recent_reactions", "popular_reactions", "allow_custom_emoji", "are_tags", "unavailability_reason", "_extra", "_client_id", "_type")

    def __init__(self, top_reactions: List[AvailableReaction] | None = None, recent_reactions: List[AvailableReaction] | None = None, popular_reactions: List[AvailableReaction] | None = None, allow_custom_emoji: bool = False, are_tags: bool = False, unavailability_reason: ReactionUnavailabilityReason | None = None):
        self.top_reactions = top_reactions
        self.recent_reactions = recent_reactions
        self.popular_reactions = popular_reactions
        self.allow_custom_emoji = allow_custom_emoji
        self.are_tags = are_tags
        self.unavailability_reason = unavailability_reason
        self._type = "availableReactions"