from .function import Function

from .report_story_result_ok import ReportStoryResultOk
from .report_story_result_option_required import ReportStoryResultOptionRequired
from .report_story_result_text_required import ReportStoryResultTextRequired

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class ReportStory(Function[ReportStoryResultOk | ReportStoryResultOptionRequired | ReportStoryResultTextRequired]):
    """
    Reports a story to the Telegram moderators

    :param story_poster_chat_id: The identifier of the poster of the story to report
    :param story_id: The identifier of the story to report
    :param option_id: Option identifier chosen by the user; leave empty for the initial request
    :param text: Additional report details; 0-1024 characters; leave empty for the initial request
    :return: :class:`ReportStoryResultOk | ReportStoryResultOptionRequired | ReportStoryResultTextRequired`
    """
    __slots__ = ("story_poster_chat_id", "story_id", "option_id", "text", "_extra", "_client_id", "_type")

    def __init__(self, story_poster_chat_id: int = 0, story_id: int = 0, option_id: bytes = b"", text: str = ""):
        self.story_poster_chat_id = story_poster_chat_id
        self.story_id = story_id
        self.option_id = option_id
        self.text = text
        self._type = "reportStory"