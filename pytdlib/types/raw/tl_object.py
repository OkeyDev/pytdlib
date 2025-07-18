import base64
import json
from typing import Any


class TlObject:
    __slots__ = ("_extra", "_client_id")

    def __json__(self) -> dict:
        data_dict: dict[str, Any] = {}
        for key in self.__slots__:
            value = getattr(self, key, None)
            if key in ("_extra", "_client_id", "_type"):
                key = "@" + key[1:]

            if value is None:
                continue
            elif isinstance(value, TlObject):
                data_dict[key] = value.__json__()
            elif isinstance(value, bytes):
                data_dict[key] = base64.b64encode(value).decode()
            else:
                data_dict[key] = json.dumps(value)

        return data_dict

    def __str__(self) -> str:
        params = ", ".join(
            f"{key}={getattr(self, key, None)}" for key in self.__slots__
        )
        return f"{self.__class__.__name__}({params})"
