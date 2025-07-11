from .function import Function

from .message_sender import MessageSender
from .star_transaction_direction import StarTransactionDirection
from .star_transactions import StarTransactions

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class GetStarTransactions(Function[StarTransactions]):
    """
    Returns the list of Telegram Star transactions for the specified owner

    :param owner_id: Identifier of the owner of the Telegram Stars; can be the identifier of the current user, identifier of an owned bot, or identifier of a supergroup or a channel chat with supergroupFullInfo.can_get_star_revenue_statistics == true
    :param subscription_id: If non-empty, only transactions related to the Star Subscription will be returned
    :param direction: Direction of the transactions to receive; pass null to get all transactions
    :param offset: Offset of the first transaction to return as received from the previous request; use empty string to get the first chunk of results
    :param limit: The maximum number of transactions to return
    :return: :class:`StarTransactions`
    """
    __slots__ = ("owner_id", "subscription_id", "direction", "offset", "limit", "_extra", "_client_id", "_type")

    def __init__(self, owner_id: MessageSender | None = None, subscription_id: str = "", direction: StarTransactionDirection | None = None, offset: str = "", limit: int = 0):
        self.owner_id = owner_id
        self.subscription_id = subscription_id
        self.direction = direction
        self.offset = offset
        self.limit = limit
        self._type = "getStarTransactions"