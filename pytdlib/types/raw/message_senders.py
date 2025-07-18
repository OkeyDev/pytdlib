from .object_base import ObjectBase

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class MessageSenders(ObjectBase):
    """
    Represents a list of message senders

    :param total_count: Approximate total number of messages senders found
    :param senders: List of message senders
    """
    __slots__ = ("total_count", "senders", "_extra", "_client_id", "_type")

    def __init__(self, total_count = None, senders = None):
        self.total_count = total_count
        self.senders = senders
        self._type = "messageSenders"