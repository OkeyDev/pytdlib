from .function import Function

from .ok import Ok

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class SetLogTagVerbosityLevel(Function[Ok]):
    """
    Sets the verbosity level for a specified TDLib internal log tag. Can be called synchronously

    :param tag: Logging tag to change verbosity level
    :param new_verbosity_level: New verbosity level; 1-1024
    :return: :class:`Ok`
    """
    __slots__ = ("tag", "new_verbosity_level", "_extra", "_client_id", "_type")

    def __init__(self, tag: str = "", new_verbosity_level: int = 0):
        self.tag = tag
        self.new_verbosity_level = new_verbosity_level
        self._type = "setLogTagVerbosityLevel"