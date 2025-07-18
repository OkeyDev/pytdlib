from .premium_limit_type import PremiumLimitType

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class PremiumLimitTypeSimilarChatCount(PremiumLimitType):
    """
    The maximum number of received similar chats

    """
    __slots__ = ("_extra", "_client_id", "_type")

    def __init__(self):

        self._type = "premiumLimitTypeSimilarChatCount"