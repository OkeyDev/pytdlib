from .function import Function

from .rtmp_url import RtmpUrl

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class GetVideoChatRtmpUrl(Function[RtmpUrl]):
    """
    Returns RTMP URL for streaming to the video chat of a chat; requires can_manage_video_chats administrator right

    :param chat_id: Chat identifier
    :return: :class:`RtmpUrl`
    """
    __slots__ = ("chat_id", "_extra", "_client_id", "_type")

    def __init__(self, chat_id: int = 0):
        self.chat_id = chat_id
        self._type = "getVideoChatRtmpUrl"