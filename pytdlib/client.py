import asyncio
import typing

from pytdlib.exceptions import PyTdLibResponseError
from pytdlib.library_executor import LibraryExecutor
from pytdlib.types.raw.error import Error
from pytdlib.types.raw.function import Function
from pytdlib.types.raw.tl_object import TlObject

T = typing.TypeVar("T", bound=TlObject)


class Client:
    """
    Easy way to redirect commands to tdlib. DO NOT CREATE IT BY YOURSELF.
    Use :class:`ClientManager` for that.
    """

    def __init__(
        self,
        client_id: int,
        executor: LibraryExecutor,
        loop: asyncio.AbstractEventLoop,
        result_timeout: float,
    ) -> None:
        self.id = client_id
        self._executor = executor
        self._loop = loop
        self._result_timeout = result_timeout

    # BASIC FUNCTIONS
    def send(self, command: Function[T]) -> None:
        """
        Send command and do not wait result. You can process the answer via `ClientManager.add_handler`.
        """

        self._executor.send(self.id, command)

    async def execute(self, command: Function[T]) -> T:
        event = self._loop.create_future()

        def wait_result(execution_result: T | Error):
            self._loop.call_soon_threadsafe(event.set_result, execution_result)

        self._executor.send(
            client_id=self.id, command=command, callback_function=wait_result
        )
        async with asyncio.timeout(self._result_timeout):
            result = await event

        if isinstance(result, Error):
            raise PyTdLibResponseError(command, result.code, result.message)

        return result
