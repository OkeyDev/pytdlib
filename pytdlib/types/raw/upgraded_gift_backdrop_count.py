from .object_base import ObjectBase

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class UpgradedGiftBackdropCount(ObjectBase):
    """
    Describes a backdrop of an upgraded gift

    :param backdrop: The backdrop
    :param total_count: Total number of gifts with the symbol
    """
    __slots__ = ("backdrop", "total_count", "_extra", "_client_id", "_type")

    def __init__(self, backdrop = None, total_count = None):
        self.backdrop = backdrop
        self.total_count = total_count
        self._type = "upgradedGiftBackdropCount"