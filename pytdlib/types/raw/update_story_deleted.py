from .update import Update

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class UpdateStoryDeleted(Update):
    """
    A story became inaccessible

    :param story_poster_chat_id: Identifier of the chat that posted the story
    :param story_id: Story identifier
    """
    __slots__ = ("story_poster_chat_id", "story_id", "_extra", "_client_id", "_type")

    def __init__(self, story_poster_chat_id = None, story_id = None):
        self.story_poster_chat_id = story_poster_chat_id
        self.story_id = story_id
        self._type = "updateStoryDeleted"