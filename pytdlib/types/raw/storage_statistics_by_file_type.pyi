from .file_type import FileType
from .object_base import ObjectBase

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class StorageStatisticsByFileType(ObjectBase):
    """
    Contains the storage usage statistics for a specific file type

    :param file_type: File type
    :param size: Total size of the files, in bytes
    :param count: Total number of files
    """
    __slots__ = ("file_type", "size", "count", "_extra", "_client_id", "_type")

    def __init__(self, file_type: FileType | None = None, size: int = 0, count: int = 0):
        self.file_type = file_type
        self.size = size
        self.count = count
        self._type = "storageStatisticsByFileType"