from .object_base import ObjectBase

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class MessagePositions(ObjectBase):
    """
    Contains a list of message positions

    :param total_count: Total number of messages found
    :param positions: List of message positions
    """
    __slots__ = ("total_count", "positions", "_extra", "_client_id", "_type")

    def __init__(self, total_count = None, positions = None):
        self.total_count = total_count
        self.positions = positions
        self._type = "messagePositions"