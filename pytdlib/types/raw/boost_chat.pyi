from .function import Function

from .chat_boost_slots import ChatBoostSlots
from typing import List

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class BoostChat(Function[ChatBoostSlots]):
    """
    Boosts a chat and returns the list of available chat boost slots for the current user after the boost

    :param chat_id: Identifier of the chat
    :param slot_ids: Identifiers of boost slots of the current user from which to apply boosts to the chat
    :return: :class:`ChatBoostSlots`
    """
    __slots__ = ("chat_id", "slot_ids", "_extra", "_client_id", "_type")

    def __init__(self, chat_id: int = 0, slot_ids: List[int] | None = None):
        self.chat_id = chat_id
        self.slot_ids = slot_ids
        self._type = "boostChat"