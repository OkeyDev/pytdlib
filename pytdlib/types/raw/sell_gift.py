from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class SellGift(Function):
    """
    Sells a gift for Telegram Stars

    :param business_connection_id: Unique identifier of business connection on behalf of which to send the request; for bots only
    :param received_gift_id: Identifier of the gift
    :return: :class:`Ok`
    """
    __slots__ = ("business_connection_id", "received_gift_id", "_extra", "_client_id", "_type")

    def __init__(self, business_connection_id = None, received_gift_id = None):
        self.business_connection_id = business_connection_id
        self.received_gift_id = received_gift_id
        self._type = "sellGift"