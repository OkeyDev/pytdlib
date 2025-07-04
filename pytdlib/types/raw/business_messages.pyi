from .business_message import BusinessMessage
from .object_base import ObjectBase
from typing import List

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class BusinessMessages(ObjectBase):
    """
    Contains a list of messages from a business account as received by a bot

    :param messages: List of business messages
    """
    __slots__ = ("messages", "_extra", "_client_id", "_type")

    def __init__(self, messages: List[BusinessMessage] | None = None):
        self.messages = messages
        self._type = "businessMessages"