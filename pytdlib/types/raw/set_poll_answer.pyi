from .function import Function

from .ok import Ok
from typing import List

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class SetPollAnswer(Function[Ok]):
    """
    Changes the user answer to a poll. A poll in quiz mode can be answered only once

    :param chat_id: Identifier of the chat to which the poll belongs
    :param message_id: Identifier of the message containing the poll
    :param option_ids: 0-based identifiers of answer options, chosen by the user. User can choose more than 1 answer option only is the poll allows multiple answers
    :return: :class:`Ok`
    """
    __slots__ = ("chat_id", "message_id", "option_ids", "_extra", "_client_id", "_type")

    def __init__(self, chat_id: int = 0, message_id: int = 0, option_ids: List[int] | None = None):
        self.chat_id = chat_id
        self.message_id = message_id
        self.option_ids = option_ids
        self._type = "setPollAnswer"