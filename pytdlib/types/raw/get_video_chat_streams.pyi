from .function import Function

from .video_chat_streams import VideoChatStreams

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class GetVideoChatStreams(Function[VideoChatStreams]):
    """
    Returns information about available video chat streams

    :param group_call_id: Group call identifier
    :return: :class:`VideoChatStreams`
    """
    __slots__ = ("group_call_id", "_extra", "_client_id", "_type")

    def __init__(self, group_call_id: int = 0):
        self.group_call_id = group_call_id
        self._type = "getVideoChatStreams"