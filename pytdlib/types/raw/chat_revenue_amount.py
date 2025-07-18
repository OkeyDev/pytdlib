from .object_base import ObjectBase

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class ChatRevenueAmount(ObjectBase):
    """
    Contains information about revenue earned from sponsored messages in a chat

    :param cryptocurrency: Cryptocurrency in which revenue is calculated
    :param total_amount: Total amount of the cryptocurrency earned, in the smallest units of the cryptocurrency
    :param balance_amount: Amount of the cryptocurrency that isn't withdrawn yet, in the smallest units of the cryptocurrency
    :param available_amount: Amount of the cryptocurrency available for withdrawal, in the smallest units of the cryptocurrency
    :param withdrawal_enabled: True, if Telegram Stars can be withdrawn now or later
    """
    __slots__ = ("cryptocurrency", "total_amount", "balance_amount", "available_amount", "withdrawal_enabled", "_extra", "_client_id", "_type")

    def __init__(self, cryptocurrency = None, total_amount = None, balance_amount = None, available_amount = None, withdrawal_enabled = None):
        self.cryptocurrency = cryptocurrency
        self.total_amount = total_amount
        self.balance_amount = balance_amount
        self.available_amount = available_amount
        self.withdrawal_enabled = withdrawal_enabled
        self._type = "chatRevenueAmount"