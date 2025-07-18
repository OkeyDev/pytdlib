from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class GetChatStoryInteractions(Function):
    """
    Returns interactions with a story posted in a chat. Can be used only if story is posted on behalf of a chat and the user is an administrator in the chat

    :param story_poster_chat_id: The identifier of the poster of the story
    :param story_id: Story identifier
    :param reaction_type: Pass the default heart reaction or a suggested reaction type to receive only interactions with the specified reaction type; pass null to receive all interactions; reactionTypePaid isn't supported
    :param prefer_forwards: Pass true to get forwards and reposts first, then reactions, then other views; pass false to get interactions sorted just by interaction date
    :param offset: Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results
    :param limit: The maximum number of story interactions to return
    :return: :class:`StoryInteractions`
    """
    __slots__ = ("story_poster_chat_id", "story_id", "reaction_type", "prefer_forwards", "offset", "limit", "_extra", "_client_id", "_type")

    def __init__(self, story_poster_chat_id = None, story_id = None, reaction_type = None, prefer_forwards = None, offset = None, limit = None):
        self.story_poster_chat_id = story_poster_chat_id
        self.story_id = story_id
        self.reaction_type = reaction_type
        self.prefer_forwards = prefer_forwards
        self.offset = offset
        self.limit = limit
        self._type = "getChatStoryInteractions"