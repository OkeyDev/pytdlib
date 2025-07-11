from .function import Function

from .database_statistics import DatabaseStatistics

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class GetDatabaseStatistics(Function[DatabaseStatistics]):
    """
    Returns database statistics

    :return: :class:`DatabaseStatistics`
    """
    __slots__ = ("_extra", "_client_id", "_type")

    def __init__(self):

        self._type = "getDatabaseStatistics"