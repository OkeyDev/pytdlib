from .function import Function

from .ok import Ok
from .story_list import StoryList

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class SetChatActiveStoriesList(Function[Ok]):
    """
    Changes story list in which stories from the chat are shown

    :param chat_id: Identifier of the chat that posted stories
    :param story_list: New list for active stories posted by the chat
    :return: :class:`Ok`
    """
    __slots__ = ("chat_id", "story_list", "_extra", "_client_id", "_type")

    def __init__(self, chat_id: int = 0, story_list: StoryList | None = None):
        self.chat_id = chat_id
        self.story_list = story_list
        self._type = "setChatActiveStoriesList"