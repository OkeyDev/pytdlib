from .input_inline_query_result import InputInlineQueryResult
from .reply_markup import ReplyMarkup

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class InputInlineQueryResultGame(InputInlineQueryResult):
    """
    Represents a game

    :param id: Unique identifier of the query result
    :param game_short_name: Short name of the game
    :param reply_markup: The message reply markup; pass null if none. Must be of type replyMarkupInlineKeyboard or null
    """
    __slots__ = ("id", "game_short_name", "reply_markup", "_extra", "_client_id", "_type")

    def __init__(self, id: str = "", game_short_name: str = "", reply_markup: ReplyMarkup | None = None):
        self.id = id
        self.game_short_name = game_short_name
        self.reply_markup = reply_markup
        self._type = "inputInlineQueryResultGame"