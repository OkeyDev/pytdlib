from .function import Function

from .affiliate_type import AffiliateType
from .connected_affiliate_program import ConnectedAffiliateProgram

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class ConnectAffiliateProgram(Function[ConnectedAffiliateProgram]):
    """
    Connects an affiliate program to the given affiliate. Returns information about the connected affiliate program

    :param affiliate: The affiliate to which the affiliate program will be connected
    :param bot_user_id: Identifier of the bot, which affiliate program is connected
    :return: :class:`ConnectedAffiliateProgram`
    """
    __slots__ = ("affiliate", "bot_user_id", "_extra", "_client_id", "_type")

    def __init__(self, affiliate: AffiliateType | None = None, bot_user_id: int = 0):
        self.affiliate = affiliate
        self.bot_user_id = bot_user_id
        self._type = "connectAffiliateProgram"