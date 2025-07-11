from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class CloseStory(Function):
    """
    Informs TDLib that a story is closed by the user

    :param story_poster_chat_id: The identifier of the poster of the story to close
    :param story_id: The identifier of the story
    :return: :class:`Ok`
    """
    __slots__ = ("story_poster_chat_id", "story_id", "_extra", "_client_id", "_type")

    def __init__(self, story_poster_chat_id = None, story_id = None):
        self.story_poster_chat_id = story_poster_chat_id
        self.story_id = story_id
        self._type = "closeStory"