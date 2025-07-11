from .function import Function

from .storage_statistics_fast import StorageStatisticsFast

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class GetStorageStatisticsFast(Function[StorageStatisticsFast]):
    """
    Quickly returns approximate storage usage statistics. Can be called before authorization

    :return: :class:`StorageStatisticsFast`
    """
    __slots__ = ("_extra", "_client_id", "_type")

    def __init__(self):

        self._type = "getStorageStatisticsFast"