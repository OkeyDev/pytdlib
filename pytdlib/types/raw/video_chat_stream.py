from .object_base import ObjectBase

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class VideoChatStream(ObjectBase):
    """
    Describes an available stream in a video chat

    :param channel_id: Identifier of an audio/video channel
    :param scale: Scale of segment durations in the stream. The duration is 1000/(2**scale) milliseconds
    :param time_offset: Point in time when the stream currently ends; Unix timestamp in milliseconds
    """
    __slots__ = ("channel_id", "scale", "time_offset", "_extra", "_client_id", "_type")

    def __init__(self, channel_id = None, scale = None, time_offset = None):
        self.channel_id = channel_id
        self.scale = scale
        self.time_offset = time_offset
        self._type = "videoChatStream"