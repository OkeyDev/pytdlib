from .link_preview_type import LinkPreviewType

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class LinkPreviewTypeStory(LinkPreviewType):
    """
    The link is a link to a story. Link preview description is unavailable

    :param story_poster_chat_id: The identifier of the chat that posted the story
    :param story_id: Story identifier
    """
    __slots__ = ("story_poster_chat_id", "story_id", "_extra", "_client_id", "_type")

    def __init__(self, story_poster_chat_id: int = 0, story_id: int = 0):
        self.story_poster_chat_id = story_poster_chat_id
        self.story_id = story_id
        self._type = "linkPreviewTypeStory"