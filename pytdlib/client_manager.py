import asyncio
import logging
import re
import time
import typing
from collections import defaultdict

from pytdlib.client import Client
from pytdlib.json_hooks import to_object_hook
from pytdlib.library_executor import LibraryExecutor
from pytdlib.log import ClientLogAdapter
from pytdlib.types.raw.authorization_state_wait_phone_number import (
    AuthorizationStateWaitPhoneNumber,
)
from pytdlib.types.raw.authorization_state_wait_tdlib_parameters import (
    AuthorizationStateWaitTdlibParameters,
)
from pytdlib.types.raw.check_authentication_bot_token import CheckAuthenticationBotToken
from pytdlib.types.raw.get_authorization_state import GetAuthorizationState
from pytdlib.types.raw.object_base import ObjectBase
from pytdlib.types.raw.set_authentication_phone_number import (
    SetAuthenticationPhoneNumber,
)
from pytdlib.types.raw.set_log_verbosity_level import SetLogVerbosityLevel
from pytdlib.types.raw.set_tdlib_parameters import SetTdlibParameters
from pytdlib.types.raw.tl_object import TlObject
from pytdlib.types.raw.update_authorization_state import UpdateAuthorizationState
from pytdlib.utils import filter_mobile_phone

BOT_TOKEN_REGEX = re.compile(r"[0-9]{8,12}:[a-zA-Z0-9_-]{35}")

logger = logging.getLogger(__name__)

T = typing.TypeVar("T")


class Handler:
    def __init__(
        self,
        function: typing.Callable[..., typing.Awaitable],
        extra: dict[str, typing.Any],
    ) -> None:
        self.function = function
        self.extra = extra

    async def execute(self, client: Client, obj: ObjectBase):
        client_logger = ClientLogAdapter(logger, dict(client_id=client.id))
        try:
            start_time = time.time()
            await self.function(client, obj, **self.extra)
            end_time = time.time()
            client_logger.info(
                "Handler %s processed in %d ms",
                self,
                int((end_time - start_time) * 1000),
            )
        except Exception:
            client_logger.exception("Error in handler %s with object %s", self, obj)

    def __str__(self) -> str:
        return f"Handler({self.function}, {self.extra})"


class ClientManager:
    def __init__(
        self,
        executor: LibraryExecutor,
        default_tdlib_params: SetTdlibParameters,
        result_timeout: float = 60,
        td_log_level: int = 2,
        loop: asyncio.AbstractEventLoop | None = None,
    ) -> None:
        self.executor = executor
        self.executor.set_default_handler(self.default_handler)
        self.executor.execute(SetLogVerbosityLevel(new_verbosity_level=td_log_level))

        self.default_tdlib_params = default_tdlib_params
        self.result_timeout = result_timeout
        if loop is not None:
            self.loop = loop
        else:
            self.loop = asyncio.get_event_loop()

        self.id_clients: dict[int, Client] = {}
        self.account_clients: dict[str, Client] = {}
        self.auth_events = defaultdict(asyncio.Event)

        self.handlers: dict[typing.Type, list[Handler]] = defaultdict(list)

        self.add_handler(UpdateAuthorizationState, self._authorize_handler)

        self.executor.start_listening()

    async def _create_client(self, set_params: SetTdlibParameters, phone_or_token: str):
        client_id = self.executor.create_client()
        # phone_or_token должен быть тут, иначе во время выполнения get_or_create_client
        # с разных корутин может создаться два одинаковых клиента.
        self.id_clients[client_id] = self.account_clients[phone_or_token] = client = (
            Client(client_id, self.executor, self.loop, self.result_timeout)
        )
        await client.execute(set_params)
        command = GetAuthorizationState()
        current_state = await client.execute(command)
        if isinstance(current_state, AuthorizationStateWaitPhoneNumber):
            if BOT_TOKEN_REGEX.match(phone_or_token):
                await client.execute(CheckAuthenticationBotToken(token=phone_or_token))
            else:
                # TODO: Add ability to set settings
                await client.execute(
                    SetAuthenticationPhoneNumber(phone_number=phone_or_token)
                )

        client_logger = ClientLogAdapter(logger, dict(client_id=client.id))
        client_logger.info("Client created: %s", phone_or_token)

        return client

    def _generate_set_tdlib_params(
        self, phone_or_token: str, **kwargs
    ) -> SetTdlibParameters:
        default_params = self.default_tdlib_params.__json__()
        default_params["database_directory"] += f"/{phone_or_token}"
        default_params.update(kwargs)
        return typing.cast(SetTdlibParameters, to_object_hook(default_params))

    async def get_or_create_client(self, phone_or_token: str, **kwargs):
        # TODO: Придумать как по адекватному сделать изменения tdlib параметров
        """
        Finds clients in created by `phone_or_token`, return it if found otherwise creates new.

        :param phone_or_token: provide bot token for bots and phone number for telegram accounts.
            bot will be activated automatically. For telegram account you need to eneter data based on `Client.get_auth_state`.
        :param kwargs: provide custom data for tdlib params.
        """
        if not BOT_TOKEN_REGEX.match(phone_or_token):
            phone_or_token = filter_mobile_phone(phone_or_token)
        client = self.account_clients.get(phone_or_token)
        if client is None:
            set_params = self._generate_set_tdlib_params(phone_or_token, **kwargs)
            client = await self._create_client(set_params, phone_or_token)

        await self.auth_events[client.id].wait()

        return client

    def add_handler(
        self,
        obj: typing.Type[TlObject],
        function: typing.Callable[..., typing.Awaitable],
        **kwargs,
    ):
        self.handlers[obj].append(Handler(function, kwargs))

    def default_handler(self, obj: ObjectBase):
        assert obj._client_id
        handlers = self.handlers[obj.__class__]
        for h in handlers:
            client = self.id_clients[obj._client_id]
            asyncio.run_coroutine_threadsafe(h.execute(client, obj), self.loop)
        logger.debug("%s handlers was emmited on update %s", len(handlers), obj)

    async def _authorize_handler(self, _, auth_state: UpdateAuthorizationState):
        if not isinstance(auth_state, AuthorizationStateWaitTdlibParameters):
            self.auth_events[auth_state._client_id].set()
            logger.info(
                "Updated auth state for %s to %s",
                auth_state._client_id,
                auth_state.authorization_state,
            )
