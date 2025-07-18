from .function import Function

from .found_stories import FoundStories
from .location_address import LocationAddress

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class SearchPublicStoriesByLocation(Function[FoundStories]):
    """
    Searches for public stories by the given address location. For optimal performance, the number of returned stories is chosen by TDLib and can be smaller than the specified limit

    :param address: Address of the location
    :param offset: Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results
    :param limit: The maximum number of stories to be returned; up to 100. For optimal performance, the number of returned stories is chosen by TDLib and can be smaller than the specified limit
    :return: :class:`FoundStories`
    """
    __slots__ = ("address", "offset", "limit", "_extra", "_client_id", "_type")

    def __init__(self, address: LocationAddress | None = None, offset: str = "", limit: int = 0):
        self.address = address
        self.offset = offset
        self.limit = limit
        self._type = "searchPublicStoriesByLocation"