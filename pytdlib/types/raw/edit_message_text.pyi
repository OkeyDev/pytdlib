from .function import Function

from .input_message_content import InputMessageContent
from .message import Message
from .reply_markup import ReplyMarkup

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class EditMessageText(Function[Message]):
    """
    Edits the text of a message (or a text of a game message). Returns the edited message after the edit is completed on the server side

    :param chat_id: The chat the message belongs to
    :param message_id: Identifier of the message. Use messageProperties.can_be_edited to check whether the message can be edited
    :param reply_markup: The new message reply markup; pass null if none; for bots only
    :param input_message_content: New text content of the message. Must be of type inputMessageText
    :return: :class:`Message`
    """
    __slots__ = ("chat_id", "message_id", "reply_markup", "input_message_content", "_extra", "_client_id", "_type")

    def __init__(self, chat_id: int = 0, message_id: int = 0, reply_markup: ReplyMarkup | None = None, input_message_content: InputMessageContent | None = None):
        self.chat_id = chat_id
        self.message_id = message_id
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
        self._type = "editMessageText"