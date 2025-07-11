from .update import Update

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class UpdateConnectionState(Update):
    """
    The connection state has changed. This update must be used only to show a human-readable description of the connection state

    :param state: The new connection state
    """
    __slots__ = ("state", "_extra", "_client_id", "_type")

    def __init__(self, state = None):
        self.state = state
        self._type = "updateConnectionState"