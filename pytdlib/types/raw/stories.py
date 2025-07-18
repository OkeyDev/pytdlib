from .object_base import ObjectBase

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class Stories(ObjectBase):
    """
    Represents a list of stories

    :param total_count: Approximate total number of stories found
    :param stories: The list of stories
    :param pinned_story_ids: Identifiers of the pinned stories; returned only in getChatPostedToChatPageStories with from_story_id == 0
    """
    __slots__ = ("total_count", "stories", "pinned_story_ids", "_extra", "_client_id", "_type")

    def __init__(self, total_count = None, stories = None, pinned_story_ids = None):
        self.total_count = total_count
        self.stories = stories
        self.pinned_story_ids = pinned_story_ids
        self._type = "stories"