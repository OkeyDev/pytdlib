from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class SetAutoDownloadSettings(Function):
    """
    Sets auto-download settings

    :param settings: New user auto-download settings
    :param type: Type of the network for which the new settings are relevant
    :return: :class:`Ok`
    """
    __slots__ = ("settings", "type", "_extra", "_client_id", "_type")

    def __init__(self, settings = None, type = None):
        self.settings = settings
        self.type = type
        self._type = "setAutoDownloadSettings"