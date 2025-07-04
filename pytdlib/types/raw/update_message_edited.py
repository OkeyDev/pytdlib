from .update import Update

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class UpdateMessageEdited(Update):
    """
    A message was edited. Changes in the message content will come in a separate updateMessageContent

    :param chat_id: Chat identifier
    :param message_id: Message identifier
    :param edit_date: Point in time (Unix timestamp) when the message was edited
    :param reply_markup: New message reply markup; may be null
    """
    __slots__ = ("chat_id", "message_id", "edit_date", "reply_markup", "_extra", "_client_id", "_type")

    def __init__(self, chat_id = None, message_id = None, edit_date = None, reply_markup = None):
        self.chat_id = chat_id
        self.message_id = message_id
        self.edit_date = edit_date
        self.reply_markup = reply_markup
        self._type = "updateMessageEdited"