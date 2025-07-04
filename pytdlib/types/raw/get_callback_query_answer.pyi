from .function import Function

from .callback_query_answer import CallbackQueryAnswer
from .callback_query_payload import CallbackQueryPayload

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class GetCallbackQueryAnswer(Function[CallbackQueryAnswer]):
    """
    Sends a callback query to a bot and returns an answer. Returns an error with code 502 if the bot fails to answer the query before the query timeout expires

    :param chat_id: Identifier of the chat with the message
    :param message_id: Identifier of the message from which the query originated. The message must not be scheduled
    :param payload: Query payload
    :return: :class:`CallbackQueryAnswer`
    """
    __slots__ = ("chat_id", "message_id", "payload", "_extra", "_client_id", "_type")

    def __init__(self, chat_id: int = 0, message_id: int = 0, payload: CallbackQueryPayload | None = None):
        self.chat_id = chat_id
        self.message_id = message_id
        self.payload = payload
        self._type = "getCallbackQueryAnswer"