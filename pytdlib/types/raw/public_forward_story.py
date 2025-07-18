from .public_forward import PublicForward

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class PublicForwardStory(PublicForward):
    """
    Contains a public repost to a story

    :param story: Information about the story
    """
    __slots__ = ("story", "_extra", "_client_id", "_type")

    def __init__(self, story = None):
        self.story = story
        self._type = "publicForwardStory"