from .paid_reaction_type import PaidReactionType
from .update import Update

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class UpdateDefaultPaidReactionType(Update):
    """
    The type of default paid reaction has changed

    :param type: The new type of the default paid reaction
    """
    __slots__ = ("type", "_extra", "_client_id", "_type")

    def __init__(self, type: PaidReactionType | None = None):
        self.type = type
        self._type = "updateDefaultPaidReactionType"