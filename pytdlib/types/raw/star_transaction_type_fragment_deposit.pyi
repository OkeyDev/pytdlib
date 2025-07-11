from .star_transaction_type import StarTransactionType

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class StarTransactionTypeFragmentDeposit(StarTransactionType):
    """
    The transaction is a deposit of Telegram Stars from Fragment; for regular users and bots only

    """
    __slots__ = ("_extra", "_client_id", "_type")

    def __init__(self):

        self._type = "starTransactionTypeFragmentDeposit"