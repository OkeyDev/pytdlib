from .paid_media import PaidMedia
from .star_transaction_type import StarTransactionType
from typing import List

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class StarTransactionTypeChannelPaidMediaPurchase(StarTransactionType):
    """
    The transaction is a purchase of paid media from a channel by the current user; for regular users only

    :param chat_id: Identifier of the channel chat that sent the paid media
    :param message_id: Identifier of the corresponding message with paid media; can be 0 or an identifier of a deleted message
    :param media: The bought media if the transaction wasn't refunded
    """
    __slots__ = ("chat_id", "message_id", "media", "_extra", "_client_id", "_type")

    def __init__(self, chat_id: int = 0, message_id: int = 0, media: List[PaidMedia] | None = None):
        self.chat_id = chat_id
        self.message_id = message_id
        self.media = media
        self._type = "starTransactionTypeChannelPaidMediaPurchase"