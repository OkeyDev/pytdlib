from ctypes import CDLL, c_char_p, c_double, c_int
from pathlib import Path

from pytdlib.exceptions import PyTdLibraryLoadException


def validate_lib_path(path: str):
    # TODO: Add windows support
    current_path = Path(path)
    if current_path.is_dir():
        current_path = current_path / "lib" / "libtdjson.so"

    return str(current_path)


def open_library(path: str):
    # TODO: Add windows support
    # TODO: Add possibility to pass installed in system lib name
    path = validate_lib_path(path)
    try:
        library = CDLL(path)
        wrapper = _TDLibWrapper(library)
        return TDLibWrapper(wrapper)
    except Exception:
        raise PyTdLibraryLoadException(path)


class _TDLibWrapper:
    def __init__(self, library: CDLL) -> None:
        self.lib = library

        self.client_create = self.lib.td_create_client_id
        self.client_create.argtypes = []
        self.client_create.restype = c_int

        self.json_client_send = self.lib.td_send
        self.json_client_send.argtypes = [c_int, c_char_p]
        self.json_client_send.restype = None

        self.json_client_receive = self.lib.td_receive
        self.json_client_receive.argtypes = [c_double]
        self.json_client_receive.restype = c_char_p

        self.json_client_execute = self.lib.td_execute
        self.json_client_execute.argtypes = [c_char_p]
        self.json_client_execute.restype = c_char_p


class TDLibWrapper:
    def __init__(self, wrapper: _TDLibWrapper) -> None:
        self.wrapper = wrapper

    def create_client(self) -> int:
        return self.wrapper.client_create()

    def send(self, client_id: int, request: bytes) -> None:
        self.wrapper.json_client_send(client_id, request)

    def receive(self, timeout: float) -> bytes:
        return self.wrapper.json_client_receive(timeout)

    def execute(self, request: bytes) -> bytes:
        return self.wrapper.json_client_execute(request)
