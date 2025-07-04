from .function import Function

from .ok import Ok
from .proxy_type import ProxyType

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class TestProxy(Function[Ok]):
    """
    Sends a simple network request to the Telegram servers via proxy; for testing only. Can be called before authorization

    :param server: Proxy server domain or IP address
    :param port: Proxy server port
    :param type: Proxy type
    :param dc_id: Identifier of a datacenter with which to test connection
    :param timeout: The maximum overall timeout for the request
    :return: :class:`Ok`
    """
    __slots__ = ("server", "port", "type", "dc_id", "timeout", "_extra", "_client_id", "_type")

    def __init__(self, server: str = "", port: int = 0, type: ProxyType | None = None, dc_id: int = 0, timeout: float = 0):
        self.server = server
        self.port = port
        self.type = type
        self.dc_id = dc_id
        self.timeout = timeout
        self._type = "testProxy"