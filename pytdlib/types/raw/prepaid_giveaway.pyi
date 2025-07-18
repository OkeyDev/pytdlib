from .giveaway_prize import GiveawayPrize
from .object_base import ObjectBase

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class PrepaidGiveaway(ObjectBase):
    """
    Describes a prepaid giveaway

    :param id: Unique identifier of the prepaid giveaway
    :param winner_count: Number of users which will receive giveaway prize
    :param prize: Prize of the giveaway
    :param boost_count: The number of boosts received by the chat from the giveaway; for Telegram Star giveaways only
    :param payment_date: Point in time (Unix timestamp) when the giveaway was paid
    """
    __slots__ = ("id", "winner_count", "prize", "boost_count", "payment_date", "_extra", "_client_id", "_type")

    def __init__(self, id: int = 0, winner_count: int = 0, prize: GiveawayPrize | None = None, boost_count: int = 0, payment_date: int = 0):
        self.id = id
        self.winner_count = winner_count
        self.prize = prize
        self.boost_count = boost_count
        self.payment_date = payment_date
        self._type = "prepaidGiveaway"