from .function import Function

from .ok import Ok

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class CancelPreliminaryUploadFile(Function[Ok]):
    """
    Stops the preliminary uploading of a file. Supported only for files uploaded by using preliminaryUploadFile

    :param file_id: Identifier of the file to stop uploading
    :return: :class:`Ok`
    """
    __slots__ = ("file_id", "_extra", "_client_id", "_type")

    def __init__(self, file_id: int = 0):
        self.file_id = file_id
        self._type = "cancelPreliminaryUploadFile"