from .function import Function

from .ok import Ok

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class DeleteSavedCredentials(Function[Ok]):
    """
    Deletes saved credentials for all payment provider bots

    :return: :class:`Ok`
    """
    __slots__ = ("_extra", "_client_id", "_type")

    def __init__(self):

        self._type = "deleteSavedCredentials"