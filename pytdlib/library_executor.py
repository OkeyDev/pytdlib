import importlib
import json
import logging
from threading import Thread
from typing import Callable, Type, TypeVar

from pytdlib.exceptions import PyTdLibClosed
from pytdlib.json_hooks import to_object_hook
from pytdlib.types.raw.close import Close
from pytdlib.types.raw.error import Error
from pytdlib.types.raw.function import Function
from pytdlib.types.raw.object_base import ObjectBase
from pytdlib.types.raw.tl_object import TlObject
from pytdlib.utils import get_class_relative_import
from pytdlib.wrapper import TDLibWrapper

T = TypeVar("T", bound=TlObject)

logger = logging.getLogger(__name__)


FUNCTION_CALLABLE = Callable[[T | Error], None]


def _dump_model(task: Function, include_request_id: int | None = None) -> bytes:
    dumped_task = task.__json__()
    if include_request_id:
        dumped_task["@extra"] = include_request_id
    return json.dumps(dumped_task).encode()


class Handler[T]:
    def __init__(self, function: FUNCTION_CALLABLE, return_type: Type[T]) -> None:
        self.function = function
        self.return_type = return_type


class LibraryExecutor:
    def __init__(self, library: TDLibWrapper, timeout: float = 60.0) -> None:
        self.library = library
        self.timeout = timeout

        self.handlers: dict[int | None, FUNCTION_CALLABLE] = {}
        self.request_id = 0

        # https://stackoverflow.com/questions/190010/daemon-threads-explanation
        self.worker = Thread(target=self._listener, daemon=True)

        self.closed = False

    def _check_closed(self):
        if self.closed:
            raise PyTdLibClosed()

    def _next_request_id(self):
        self.request_id += 1
        return self.request_id

    def set_default_handler(self, handler: Callable[[ObjectBase], None]):
        previous_handler = self.handlers.get(None, None)
        self.handlers[None] = new_handler = handler  # type: ignore
        logger.debug(
            "Changed default handler from %s to %s", previous_handler, new_handler
        )

    def create_client(self):
        """
        Executes library `td_create_client_id` function to create client.

        client id required by :function:`send` function.
        """
        self._check_closed()
        client_id = self.library.create_client()
        logger.debug("Client with id %d created", client_id)
        return client_id

    def execute(self, task: Function):
        """
        Send command to library. Accept only function with "Can be called synchronously" in description.
        Otherwise TdLib will return error.
        """
        dumped_task = _dump_model(task)
        self.library.execute(dumped_task)
        logger.debug("Task %s executed", dumped_task)

    def send(
        self,
        client_id: int,
        command: Function[T],
        callback_function: Callable[[T | Error], None] | None = None,
    ):
        """
        Send command to tdlib and return result in `callback_function`.
        WARNING. `callback_function` executes in another thread.

        :param client_id: client id by :function:`create_client`.
        :param command: command to execute
        :param callback_function: function executes in another thread to process result (error or object)
        """
        self._check_closed()
        if callback_function:
            request_id = self._next_request_id()
            self.handlers[request_id] = callback_function
        else:
            request_id = None

        dumped_task = _dump_model(command, include_request_id=request_id)

        self.library.send(client_id, dumped_task)
        logger.debug(
            "Sent %s with request_id %s to client %s",
            dumped_task,
            request_id,
            client_id,
        )

    def start_listening(self):
        self.worker.start()

    def close(self):
        """
        Closes the tdlib instance. Should be called for gracefully shutdown.
        """

        if self.closed:
            return
        self.closed = True
        self.execute(Close())
        self.worker.join()

    def _import_class(self, type_: str) -> Type[TlObject]:
        type_ = type_[0].upper() + type_[1:]
        import_path = get_class_relative_import(type_)
        module = importlib.import_module(import_path)
        return getattr(module, type_)

    def _listener(self):
        while not self.closed:
            dumped_result = self.library.receive(self.timeout)
            if dumped_result is None:
                continue

            try:
                model: TlObject = json.loads(dumped_result, object_hook=to_object_hook)

                request_id = getattr(model, "_extra", None)
                handler = self.handlers.get(request_id, None)

                if handler is None:
                    logger.debug(
                        "Handler not found for %s and task %s",
                        request_id,
                        dumped_result,
                    )
                    continue

                logger.debug(
                    "Task %s received and passed to handler with request_id = %s.",
                    dumped_result,
                    request_id,
                )

                handler(model)
            except Exception:
                logger.exception(
                    "Something went wrong while processing %s", dumped_result
                )
