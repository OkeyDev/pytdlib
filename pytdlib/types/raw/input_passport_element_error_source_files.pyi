from .input_passport_element_error_source import InputPassportElementErrorSource
from typing import List

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class InputPassportElementErrorSourceFiles(InputPassportElementErrorSource):
    """
    The list of attached files contains an error. The error is considered resolved when the file list changes

    :param file_hashes: Current hashes of all attached files
    """
    __slots__ = ("file_hashes", "_extra", "_client_id", "_type")

    def __init__(self, file_hashes: List[bytes] | None = None):
        self.file_hashes = file_hashes
        self._type = "inputPassportElementErrorSourceFiles"