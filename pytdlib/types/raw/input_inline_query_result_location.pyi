from .input_inline_query_result import InputInlineQueryResult
from .input_message_content import InputMessageContent
from .location import Location
from .reply_markup import ReplyMarkup

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class InputInlineQueryResultLocation(InputInlineQueryResult):
    """
    Represents a point on the map

    :param id: Unique identifier of the query result
    :param location: Location result
    :param live_period: Amount of time relative to the message sent time until the location can be updated, in seconds
    :param title: Title of the result
    :param thumbnail_url: URL of the result thumbnail, if it exists
    :param thumbnail_width: Thumbnail width, if known
    :param thumbnail_height: Thumbnail height, if known
    :param reply_markup: The message reply markup; pass null if none. Must be of type replyMarkupInlineKeyboard or null
    :param input_message_content: The content of the message to be sent. Must be one of the following types: inputMessageText, inputMessageInvoice, inputMessageLocation, inputMessageVenue or inputMessageContact
    """
    __slots__ = ("id", "location", "live_period", "title", "thumbnail_url", "thumbnail_width", "thumbnail_height", "reply_markup", "input_message_content", "_extra", "_client_id", "_type")

    def __init__(self, id: str = "", location: Location | None = None, live_period: int = 0, title: str = "", thumbnail_url: str = "", thumbnail_width: int = 0, thumbnail_height: int = 0, reply_markup: ReplyMarkup | None = None, input_message_content: InputMessageContent | None = None):
        self.id = id
        self.location = location
        self.live_period = live_period
        self.title = title
        self.thumbnail_url = thumbnail_url
        self.thumbnail_width = thumbnail_width
        self.thumbnail_height = thumbnail_height
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
        self._type = "inputInlineQueryResultLocation"