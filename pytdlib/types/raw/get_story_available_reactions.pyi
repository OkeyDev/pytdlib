from .function import Function

from .available_reactions import AvailableReactions

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class GetStoryAvailableReactions(Function[AvailableReactions]):
    """
    Returns reactions, which can be chosen for a story

    :param row_size: Number of reaction per row, 5-25
    :return: :class:`AvailableReactions`
    """
    __slots__ = ("row_size", "_extra", "_client_id", "_type")

    def __init__(self, row_size: int = 0):
        self.row_size = row_size
        self._type = "getStoryAvailableReactions"