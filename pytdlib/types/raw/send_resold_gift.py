from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class SendResoldGift(Function):
    """
    Sends an upgraded gift that is available for resale to another user or channel chat; gifts already owned by the current user must be transferred using transferGift and can't be passed to the method

    :param gift_name: Name of the upgraded gift to send
    :param owner_id: Identifier of the user or the channel chat that will receive the gift
    :param star_count: The amount of Telegram Stars required to pay for the gift
    :return: :class:`Ok`
    """
    __slots__ = ("gift_name", "owner_id", "star_count", "_extra", "_client_id", "_type")

    def __init__(self, gift_name = None, owner_id = None, star_count = None):
        self.gift_name = gift_name
        self.owner_id = owner_id
        self.star_count = star_count
        self._type = "sendResoldGift"