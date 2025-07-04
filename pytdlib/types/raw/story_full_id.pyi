from .object_base import ObjectBase

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class StoryFullId(ObjectBase):
    """
    Contains identifier of a story along with identifier of the chat that posted it

    :param poster_chat_id: Identifier of the chat that posted the story
    :param story_id: Unique story identifier among stories of the chat
    """
    __slots__ = ("poster_chat_id", "story_id", "_extra", "_client_id", "_type")

    def __init__(self, poster_chat_id: int = 0, story_id: int = 0):
        self.poster_chat_id = poster_chat_id
        self.story_id = story_id
        self._type = "storyFullId"