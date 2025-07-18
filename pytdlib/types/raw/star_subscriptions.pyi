from .object_base import ObjectBase
from .star_amount import StarAmount
from .star_subscription import StarSubscription
from typing import List

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class StarSubscriptions(ObjectBase):
    """
    Represents a list of Telegram Star subscriptions

    :param star_amount: The amount of owned Telegram Stars
    :param subscriptions: List of subscriptions for Telegram Stars
    :param required_star_count: The number of Telegram Stars required to buy to extend subscriptions expiring soon
    :param next_offset: The offset for the next request. If empty, then there are no more results
    """
    __slots__ = ("star_amount", "subscriptions", "required_star_count", "next_offset", "_extra", "_client_id", "_type")

    def __init__(self, star_amount: StarAmount | None = None, subscriptions: List[StarSubscription] | None = None, required_star_count: int = 0, next_offset: str = ""):
        self.star_amount = star_amount
        self.subscriptions = subscriptions
        self.required_star_count = required_star_count
        self.next_offset = next_offset
        self._type = "starSubscriptions"