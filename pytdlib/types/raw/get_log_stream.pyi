from .function import Function

from .log_stream_default import LogStreamDefault
from .log_stream_empty import LogStreamEmpty
from .log_stream_file import LogStreamFile

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class GetLogStream(Function[LogStreamDefault | LogStreamFile | LogStreamEmpty]):
    """
    Returns information about currently used log stream for internal logging of TDLib. Can be called synchronously

    :return: :class:`LogStreamDefault | LogStreamFile | LogStreamEmpty`
    """
    __slots__ = ("_extra", "_client_id", "_type")

    def __init__(self):

        self._type = "getLogStream"