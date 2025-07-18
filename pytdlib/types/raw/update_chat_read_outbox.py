from .update import Update

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class UpdateChatReadOutbox(Update):
    """
    Outgoing messages were read

    :param chat_id: Chat identifier
    :param last_read_outbox_message_id: Identifier of last read outgoing message
    """
    __slots__ = ("chat_id", "last_read_outbox_message_id", "_extra", "_client_id", "_type")

    def __init__(self, chat_id = None, last_read_outbox_message_id = None):
        self.chat_id = chat_id
        self.last_read_outbox_message_id = last_read_outbox_message_id
        self._type = "updateChatReadOutbox"