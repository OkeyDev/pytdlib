from .connection_state import ConnectionState

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class ConnectionStateConnecting(ConnectionState):
    """
    Establishing a connection to the Telegram servers

    """
    __slots__ = ("_extra", "_client_id", "_type")

    def __init__(self):

        self._type = "connectionStateConnecting"