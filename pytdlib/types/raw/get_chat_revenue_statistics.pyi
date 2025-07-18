from .function import Function

from .chat_revenue_statistics import ChatRevenueStatistics

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class GetChatRevenueStatistics(Function[ChatRevenueStatistics]):
    """
    Returns detailed revenue statistics about a chat. Currently, this method can be used only for channels if supergroupFullInfo.can_get_revenue_statistics == true or bots if userFullInfo.bot_info.can_get_revenue_statistics == true

    :param chat_id: Chat identifier
    :param is_dark: Pass true if a dark theme is used by the application
    :return: :class:`ChatRevenueStatistics`
    """
    __slots__ = ("chat_id", "is_dark", "_extra", "_client_id", "_type")

    def __init__(self, chat_id: int = 0, is_dark: bool = False):
        self.chat_id = chat_id
        self.is_dark = is_dark
        self._type = "getChatRevenueStatistics"