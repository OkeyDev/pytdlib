from logging import LoggerAdapter
from typing import Any, MutableMapping


class ClientLogAdapter(LoggerAdapter):
    def process(
        self, msg: Any, kwargs: MutableMapping[str, Any]
    ) -> tuple[Any, MutableMapping[str, Any]]:
        return "[Client %s] %s" % (self.extra["client_id"], msg), kwargs
