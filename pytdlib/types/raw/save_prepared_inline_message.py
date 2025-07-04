from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class SavePreparedInlineMessage(Function):
    """
    Saves an inline message to be sent by the given user; for bots only

    :param user_id: Identifier of the user
    :param result: The description of the message
    :param chat_types: Types of the chats to which the message can be sent
    :return: :class:`PreparedInlineMessageId`
    """
    __slots__ = ("user_id", "result", "chat_types", "_extra", "_client_id", "_type")

    def __init__(self, user_id = None, result = None, chat_types = None):
        self.user_id = user_id
        self.result = result
        self.chat_types = chat_types
        self._type = "savePreparedInlineMessage"