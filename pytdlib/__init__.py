import asyncio
import logging

from pytdlib.library_executor import LibraryExecutor
from pytdlib.types.raw.set_tdlib_parameters import SetTdlibParameters
from pytdlib.wrapper import open_library

from .client import Client
from .client_manager import ClientManager
from .exceptions import (
    PyTdLibClosed,
    PyTdLibException,
    PyTdLibraryLoadException,
    PyTdLibResponseError,
)

__all__ = [
    "create_client_manager",
    "Client",
    "ClientManager",
    "PyTdLibException",
    "PyTdLibClosed",
    "PyTdLibResponseError",
    "PyTdLibraryLoadException",
]

logging.getLogger("pytdlib").addHandler(logging.NullHandler())


def create_client_manager(
    library_path: str,
    default_tdlib_params: SetTdlibParameters,
    receive_update_timeout: float = 60.0,
    receive_answer_timeout: float = 600.0,
    loop: asyncio.AbstractEventLoop | None = None,
    td_log_level: int = 2,
) -> ClientManager:
    wrapper = open_library(library_path)
    executor = LibraryExecutor(wrapper, receive_update_timeout)
    return ClientManager(
        executor, default_tdlib_params, receive_answer_timeout, td_log_level, loop
    )
