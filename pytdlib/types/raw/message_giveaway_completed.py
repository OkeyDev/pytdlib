from .message_content import MessageContent

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class MessageGiveawayCompleted(MessageContent):
    """
    A giveaway without public winners has been completed for the chat

    :param giveaway_message_id: Identifier of the message with the giveaway; can be 0 if the message was deleted
    :param winner_count: Number of winners in the giveaway
    :param is_star_giveaway: True, if the giveaway is a Telegram Star giveaway
    :param unclaimed_prize_count: Number of undistributed prizes; for Telegram Premium giveaways only
    """
    __slots__ = ("giveaway_message_id", "winner_count", "is_star_giveaway", "unclaimed_prize_count", "_extra", "_client_id", "_type")

    def __init__(self, giveaway_message_id = None, winner_count = None, is_star_giveaway = None, unclaimed_prize_count = None):
        self.giveaway_message_id = giveaway_message_id
        self.winner_count = winner_count
        self.is_star_giveaway = is_star_giveaway
        self.unclaimed_prize_count = unclaimed_prize_count
        self._type = "messageGiveawayCompleted"