from .function import Function

from .count import Count

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class GetBotSimilarBotCount(Function[Count]):
    """
    Returns approximate number of bots similar to the given bot

    :param bot_user_id: User identifier of the target bot
    :param return_local: Pass true to get the number of bots without sending network requests, or -1 if the number of bots is unknown locally
    :return: :class:`Count`
    """
    __slots__ = ("bot_user_id", "return_local", "_extra", "_client_id", "_type")

    def __init__(self, bot_user_id: int = 0, return_local: bool = False):
        self.bot_user_id = bot_user_id
        self.return_local = return_local
        self._type = "getBotSimilarBotCount"