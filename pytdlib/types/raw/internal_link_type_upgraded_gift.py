from .internal_link_type import InternalLinkType

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class InternalLinkTypeUpgradedGift(InternalLinkType):
    """
    The link is a link to an upgraded gift. Call getUpgradedGift with the given name to process the link

    :param name: Name of the unique gift
    """
    __slots__ = ("name", "_extra", "_client_id", "_type")

    def __init__(self, name = None):
        self.name = name
        self._type = "internalLinkTypeUpgradedGift"