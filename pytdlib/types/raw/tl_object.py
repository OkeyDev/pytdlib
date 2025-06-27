import base64
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
                data_dict[key] = value

        return data_dict