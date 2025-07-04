from .object_base import ObjectBase
from typing import List

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class Emojis(ObjectBase):
    """
    Represents a list of emojis

    :param emojis: List of emojis
    """
    __slots__ = ("emojis", "_extra", "_client_id", "_type")

    def __init__(self, emojis: List[str] | None = None):
        self.emojis = emojis
        self._type = "emojis"