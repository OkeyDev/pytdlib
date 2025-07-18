from .story import Story
from .update import Update

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class UpdateStoryPostSucceeded(Update):
    """
    A story has been successfully posted

    :param story: The posted story
    :param old_story_id: The previous temporary story identifier
    """
    __slots__ = ("story", "old_story_id", "_extra", "_client_id", "_type")

    def __init__(self, story: Story | None = None, old_story_id: int = 0):
        self.story = story
        self.old_story_id = old_story_id
        self._type = "updateStoryPostSucceeded"