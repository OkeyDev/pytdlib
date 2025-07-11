from .file_type import FileType

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class FileTypeSecretThumbnail(FileType):
    """
    The file is a thumbnail of a file from a secret chat

    """
    __slots__ = ("_extra", "_client_id", "_type")

    def __init__(self):

        self._type = "fileTypeSecretThumbnail"