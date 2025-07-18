from .input_story_area_type import InputStoryAreaType

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class InputStoryAreaTypeFoundVenue(InputStoryAreaType):
    """
    An area pointing to a venue found by the bot getOption("venue_search_bot_username")

    :param query_id: Identifier of the inline query, used to found the venue
    :param result_id: Identifier of the inline query result
    """
    __slots__ = ("query_id", "result_id", "_extra", "_client_id", "_type")

    def __init__(self, query_id = None, result_id = None):
        self.query_id = query_id
        self.result_id = result_id
        self._type = "inputStoryAreaTypeFoundVenue"