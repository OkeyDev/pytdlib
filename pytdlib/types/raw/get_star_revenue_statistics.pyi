from .function import Function

from .message_sender import MessageSender
from .star_revenue_statistics import StarRevenueStatistics

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class GetStarRevenueStatistics(Function[StarRevenueStatistics]):
    """
    Returns detailed Telegram Star revenue statistics

    :param owner_id: Identifier of the owner of the Telegram Stars; can be identifier of the current user, an owned bot, or a supergroup or a channel chat with supergroupFullInfo.can_get_star_revenue_statistics == true
    :param is_dark: Pass true if a dark theme is used by the application
    :return: :class:`StarRevenueStatistics`
    """
    __slots__ = ("owner_id", "is_dark", "_extra", "_client_id", "_type")

    def __init__(self, owner_id: MessageSender | None = None, is_dark: bool = False):
        self.owner_id = owner_id
        self.is_dark = is_dark
        self._type = "getStarRevenueStatistics"