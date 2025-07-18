from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class ReadBusinessMessage(Function):
    """
    Reads a message on behalf of a business account; for bots only

    :param business_connection_id: Unique identifier of business connection through which the message was received
    :param chat_id: The chat the message belongs to
    :param message_id: Identifier of the message
    :return: :class:`Ok`
    """
    __slots__ = ("business_connection_id", "chat_id", "message_id", "_extra", "_client_id", "_type")

    def __init__(self, business_connection_id = None, chat_id = None, message_id = None):
        self.business_connection_id = business_connection_id
        self.chat_id = chat_id
        self.message_id = message_id
        self._type = "readBusinessMessage"