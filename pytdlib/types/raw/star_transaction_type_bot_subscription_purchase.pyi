from .product_info import ProductInfo
from .star_transaction_type import StarTransactionType

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class StarTransactionTypeBotSubscriptionPurchase(StarTransactionType):
    """
    The transaction is a purchase of a subscription from a bot or a business account by the current user; for regular users only

    :param user_id: Identifier of the bot or the business account user that created the subscription link
    :param subscription_period: The number of seconds between consecutive Telegram Star debitings
    :param product_info: Information about the bought subscription
    """
    __slots__ = ("user_id", "subscription_period", "product_info", "_extra", "_client_id", "_type")

    def __init__(self, user_id: int = 0, subscription_period: int = 0, product_info: ProductInfo | None = None):
        self.user_id = user_id
        self.subscription_period = subscription_period
        self.product_info = product_info
        self._type = "starTransactionTypeBotSubscriptionPurchase"