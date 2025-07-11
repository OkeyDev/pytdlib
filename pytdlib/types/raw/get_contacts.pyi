from .function import Function

from .users import Users

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class GetContacts(Function[Users]):
    """
    Returns all contacts of the user

    :return: :class:`Users`
    """
    __slots__ = ("_extra", "_client_id", "_type")

    def __init__(self):

        self._type = "getContacts"