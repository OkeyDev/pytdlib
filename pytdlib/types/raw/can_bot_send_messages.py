from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class CanBotSendMessages(Function):
    """
    Checks whether the specified bot can send messages to the user. Returns a 404 error if can't and the access can be granted by call to allowBotToSendMessages

    :param bot_user_id: Identifier of the target bot
    :return: :class:`Ok`
    """
    __slots__ = ("bot_user_id", "_extra", "_client_id", "_type")

    def __init__(self, bot_user_id = None):
        self.bot_user_id = bot_user_id
        self._type = "canBotSendMessages"