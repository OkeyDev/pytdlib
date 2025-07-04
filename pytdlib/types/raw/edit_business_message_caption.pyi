from .function import Function

from .business_message import BusinessMessage
from .formatted_text import FormattedText
from .reply_markup import ReplyMarkup

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class EditBusinessMessageCaption(Function[BusinessMessage]):
    """
    Edits the caption of a message sent on behalf of a business account; for bots only

    :param business_connection_id: Unique identifier of business connection on behalf of which the message was sent
    :param chat_id: The chat the message belongs to
    :param message_id: Identifier of the message
    :param reply_markup: The new message reply markup; pass null if none
    :param caption: New message content caption; pass null to remove caption; 0-getOption("message_caption_length_max") characters
    :param show_caption_above_media: Pass true to show the caption above the media; otherwise, the caption will be shown below the media. May be true only for animation, photo, and video messages
    :return: :class:`BusinessMessage`
    """
    __slots__ = ("business_connection_id", "chat_id", "message_id", "reply_markup", "caption", "show_caption_above_media", "_extra", "_client_id", "_type")

    def __init__(self, business_connection_id: str = "", chat_id: int = 0, message_id: int = 0, reply_markup: ReplyMarkup | None = None, caption: FormattedText | None = None, show_caption_above_media: bool = False):
        self.business_connection_id = business_connection_id
        self.chat_id = chat_id
        self.message_id = message_id
        self.reply_markup = reply_markup
        self.caption = caption
        self.show_caption_above_media = show_caption_above_media
        self._type = "editBusinessMessageCaption"