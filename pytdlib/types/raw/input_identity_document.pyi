from .date import Date
from .input_file import InputFile
from .object_base import ObjectBase
from typing import List

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class InputIdentityDocument(ObjectBase):
    """
    An identity document to be saved to Telegram Passport

    :param number: Document number; 1-24 characters
    :param expiration_date: Document expiration date; pass null if not applicable
    :param front_side: Front side of the document
    :param reverse_side: Reverse side of the document; only for driver license and identity card; pass null otherwise
    :param selfie: Selfie with the document; pass null if unavailable
    :param translation: List of files containing a certified English translation of the document
    """
    __slots__ = ("number", "expiration_date", "front_side", "reverse_side", "selfie", "translation", "_extra", "_client_id", "_type")

    def __init__(self, number: str = "", expiration_date: Date | None = None, front_side: InputFile | None = None, reverse_side: InputFile | None = None, selfie: InputFile | None = None, translation: List[InputFile] | None = None):
        self.number = number
        self.expiration_date = expiration_date
        self.front_side = front_side
        self.reverse_side = reverse_side
        self.selfie = selfie
        self.translation = translation
        self._type = "inputIdentityDocument"