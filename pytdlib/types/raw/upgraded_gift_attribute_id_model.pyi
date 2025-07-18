from .upgraded_gift_attribute_id import UpgradedGiftAttributeId

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class UpgradedGiftAttributeIdModel(UpgradedGiftAttributeId):
    """
    Identifier of a gift model

    :param sticker_id: Identifier of the sticker representing the model
    """
    __slots__ = ("sticker_id", "_extra", "_client_id", "_type")

    def __init__(self, sticker_id: int = 0):
        self.sticker_id = sticker_id
        self._type = "upgradedGiftAttributeIdModel"