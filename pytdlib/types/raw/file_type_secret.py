from .file_type import FileType

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class FileTypeSecret(FileType):
    """
    The file was sent to a secret chat (the file type is not known to the server)

    """
    __slots__ = ("_extra", "_client_id", "_type")

    def __init__(self):

        self._type = "fileTypeSecret"