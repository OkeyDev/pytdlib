from .object_base import ObjectBase

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class FoundPositions(ObjectBase):
    """
    Contains 0-based positions of matched objects

    :param total_count: Total number of matched objects
    :param positions: The positions of the matched objects
    """
    __slots__ = ("total_count", "positions", "_extra", "_client_id", "_type")

    def __init__(self, total_count = None, positions = None):
        self.total_count = total_count
        self.positions = positions
        self._type = "foundPositions"