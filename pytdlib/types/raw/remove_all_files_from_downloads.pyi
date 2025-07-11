from .function import Function

from .ok import Ok

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class RemoveAllFilesFromDownloads(Function[Ok]):
    """
    Removes all files from the file download list

    :param only_active: Pass true to remove only active downloads, including paused
    :param only_completed: Pass true to remove only completed downloads
    :param delete_from_cache: Pass true to delete the file from the TDLib file cache
    :return: :class:`Ok`
    """
    __slots__ = ("only_active", "only_completed", "delete_from_cache", "_extra", "_client_id", "_type")

    def __init__(self, only_active: bool = False, only_completed: bool = False, delete_from_cache: bool = False):
        self.only_active = only_active
        self.only_completed = only_completed
        self.delete_from_cache = delete_from_cache
        self._type = "removeAllFilesFromDownloads"