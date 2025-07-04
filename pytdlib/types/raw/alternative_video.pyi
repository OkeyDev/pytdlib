from .file import File
from .object_base import ObjectBase

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class AlternativeVideo(ObjectBase):
    """
    Describes an alternative re-encoded quality of a video file

    :param id: Unique identifier of the alternative video, which is used in the HLS file
    :param width: Video width
    :param height: Video height
    :param codec: Codec used for video file encoding, for example, "h264", "h265", or "av1"
    :param hls_file: HLS file describing the video
    :param video: File containing the video
    """
    __slots__ = ("id", "width", "height", "codec", "hls_file", "video", "_extra", "_client_id", "_type")

    def __init__(self, id: int = 0, width: int = 0, height: int = 0, codec: str = "", hls_file: File | None = None, video: File | None = None):
        self.id = id
        self.width = width
        self.height = height
        self.codec = codec
        self.hls_file = hls_file
        self.video = video
        self._type = "alternativeVideo"