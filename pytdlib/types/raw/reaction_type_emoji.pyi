from .reaction_type import ReactionType

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class ReactionTypeEmoji(ReactionType):
    """
    A reaction with an emoji

    :param emoji: Text representation of the reaction
    """
    __slots__ = ("emoji", "_extra", "_client_id", "_type")

    def __init__(self, emoji: str = ""):
        self.emoji = emoji
        self._type = "reactionTypeEmoji"