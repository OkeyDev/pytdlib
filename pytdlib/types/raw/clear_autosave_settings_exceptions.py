from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class ClearAutosaveSettingsExceptions(Function):
    """
    Clears the list of all autosave settings exceptions. The method is guaranteed to work only after at least one call to getAutosaveSettings

    :return: :class:`Ok`
    """
    __slots__ = ("_extra", "_client_id", "_type")

    def __init__(self):

        self._type = "clearAutosaveSettingsExceptions"