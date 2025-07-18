from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class GetGiveawayInfo(Function):
    """
    Returns information about a giveaway

    :param chat_id: Identifier of the channel chat which started the giveaway
    :param message_id: Identifier of the giveaway or a giveaway winners message in the chat
    :return: :class:`GiveawayInfoOngoing | GiveawayInfoCompleted`
    """
    __slots__ = ("chat_id", "message_id", "_extra", "_client_id", "_type")

    def __init__(self, chat_id = None, message_id = None):
        self.chat_id = chat_id
        self.message_id = message_id
        self._type = "getGiveawayInfo"