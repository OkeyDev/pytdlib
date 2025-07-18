from .passport_element_error_source import PassportElementErrorSource

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class PassportElementErrorSourceFile(PassportElementErrorSource):
    """
    The file contains an error. The error will be considered resolved when the file changes

    :param file_index: Index of a file with the error
    """
    __slots__ = ("file_index", "_extra", "_client_id", "_type")

    def __init__(self, file_index = None):
        self.file_index = file_index
        self._type = "passportElementErrorSourceFile"