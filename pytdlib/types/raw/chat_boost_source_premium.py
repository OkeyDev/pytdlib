from .chat_boost_source import ChatBoostSource

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class ChatBoostSourcePremium(ChatBoostSource):
    """
    A user with Telegram Premium subscription or gifted Telegram Premium boosted the chat

    :param user_id: Identifier of the user
    """
    __slots__ = ("user_id", "_extra", "_client_id", "_type")

    def __init__(self, user_id = None):
        self.user_id = user_id
        self._type = "chatBoostSourcePremium"