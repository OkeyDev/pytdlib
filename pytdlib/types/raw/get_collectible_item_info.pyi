from .function import Function

from .collectible_item_info import CollectibleItemInfo
from .collectible_item_type import CollectibleItemType

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class GetCollectibleItemInfo(Function[CollectibleItemInfo]):
    """
    Returns information about a given collectible item that was purchased at https://fragment.com

    :param type: Type of the collectible item. The item must be used by a user and must be visible to the current user
    :return: :class:`CollectibleItemInfo`
    """
    __slots__ = ("type", "_extra", "_client_id", "_type")

    def __init__(self, type: CollectibleItemType | None = None):
        self.type = type
        self._type = "getCollectibleItemInfo"