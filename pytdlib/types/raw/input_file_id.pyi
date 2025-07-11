from .input_file import InputFile

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class InputFileId(InputFile):
    """
    A file defined by its unique identifier

    :param id: Unique file identifier
    """
    __slots__ = ("id", "_extra", "_client_id", "_type")

    def __init__(self, id: int = 0):
        self.id = id
        self._type = "inputFileId"