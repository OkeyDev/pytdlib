from .update import Update
from .video_chat import VideoChat

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class UpdateChatVideoChat(Update):
    """
    A chat video chat state has changed

    :param chat_id: Chat identifier
    :param video_chat: New value of video_chat
    """
    __slots__ = ("chat_id", "video_chat", "_extra", "_client_id", "_type")

    def __init__(self, chat_id: int = 0, video_chat: VideoChat | None = None):
        self.chat_id = chat_id
        self.video_chat = video_chat
        self._type = "updateChatVideoChat"