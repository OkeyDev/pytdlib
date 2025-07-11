from .function import Function

from .ok import Ok
from .passport_element_type import PassportElementType

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class DeletePassportElement(Function[Ok]):
    """
    Deletes a Telegram Passport element

    :param type: Element type
    :return: :class:`Ok`
    """
    __slots__ = ("type", "_extra", "_client_id", "_type")

    def __init__(self, type: PassportElementType | None = None):
        self.type = type
        self._type = "deletePassportElement"