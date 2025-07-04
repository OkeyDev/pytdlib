from .chat_list import ChatList
from .object_base import ObjectBase
from typing import List

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class ChatLists(ObjectBase):
    """
    Contains a list of chat lists

    :param chat_lists: List of chat lists
    """
    __slots__ = ("chat_lists", "_extra", "_client_id", "_type")

    def __init__(self, chat_lists: List[ChatList] | None = None):
        self.chat_lists = chat_lists
        self._type = "chatLists"