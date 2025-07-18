from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class UpgradeGift(Function):
    """
    Upgrades a regular gift

    :param business_connection_id: Unique identifier of business connection on behalf of which to send the request; for bots only
    :param received_gift_id: Identifier of the gift
    :param keep_original_details: Pass true to keep the original gift text, sender and receiver in the upgraded gift
    :param star_count: The amount of Telegram Stars required to pay for the upgrade. It the gift has prepaid_upgrade_star_count > 0, then pass 0, otherwise, pass gift.upgrade_star_count
    :return: :class:`UpgradeGiftResult`
    """
    __slots__ = ("business_connection_id", "received_gift_id", "keep_original_details", "star_count", "_extra", "_client_id", "_type")

    def __init__(self, business_connection_id = None, received_gift_id = None, keep_original_details = None, star_count = None):
        self.business_connection_id = business_connection_id
        self.received_gift_id = received_gift_id
        self.keep_original_details = keep_original_details
        self.star_count = star_count
        self._type = "upgradeGift"