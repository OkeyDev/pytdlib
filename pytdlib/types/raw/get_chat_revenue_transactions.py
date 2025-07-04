from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class GetChatRevenueTransactions(Function):
    """
    Returns the list of revenue transactions for a chat. Currently, this method can be used only for channels if supergroupFullInfo.can_get_revenue_statistics == true or bots if userFullInfo.bot_info.can_get_revenue_statistics == true

    :param chat_id: Chat identifier
    :param offset: Number of transactions to skip
    :param limit: The maximum number of transactions to be returned; up to 200
    :return: :class:`ChatRevenueTransactions`
    """
    __slots__ = ("chat_id", "offset", "limit", "_extra", "_client_id", "_type")

    def __init__(self, chat_id = None, offset = None, limit = None):
        self.chat_id = chat_id
        self.offset = offset
        self.limit = limit
        self._type = "getChatRevenueTransactions"