from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class CanPostStory(Function):
    """
    Checks whether the current user can post a story on behalf of a chat; requires can_post_stories right for supergroup and channel chats

    :param chat_id: Chat identifier. Pass Saved Messages chat identifier when posting a story on behalf of the current user
    :return: :class:`CanPostStoryResultOk | CanPostStoryResultPremiumNeeded | CanPostStoryResultBoostNeeded | CanPostStoryResultActiveStoryLimitExceeded | CanPostStoryResultWeeklyLimitExceeded | CanPostStoryResultMonthlyLimitExceeded`
    """
    __slots__ = ("chat_id", "_extra", "_client_id", "_type")

    def __init__(self, chat_id = None):
        self.chat_id = chat_id
        self._type = "canPostStory"