from .object_base import ObjectBase
from typing import List

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class GroupCallVideoSourceGroup(ObjectBase):
    """
    Describes a group of video synchronization source identifiers

    :param semantics: The semantics of sources, one of "SIM" or "FID"
    :param source_ids: The list of synchronization source identifiers
    """
    __slots__ = ("semantics", "source_ids", "_extra", "_client_id", "_type")

    def __init__(self, semantics: str = "", source_ids: List[int] | None = None):
        self.semantics = semantics
        self.source_ids = source_ids
        self._type = "groupCallVideoSourceGroup"