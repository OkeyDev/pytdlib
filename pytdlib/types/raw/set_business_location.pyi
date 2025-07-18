from .function import Function

from .business_location import BusinessLocation
from .ok import Ok

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class SetBusinessLocation(Function[Ok]):
    """
    Changes the business location of the current user. Requires Telegram Business subscription

    :param location: The new location of the business; pass null to remove the location
    :return: :class:`Ok`
    """
    __slots__ = ("location", "_extra", "_client_id", "_type")

    def __init__(self, location: BusinessLocation | None = None):
        self.location = location
        self._type = "setBusinessLocation"