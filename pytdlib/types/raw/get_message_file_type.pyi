from .function import Function

from .message_file_type_group import MessageFileTypeGroup
from .message_file_type_private import MessageFileTypePrivate
from .message_file_type_unknown import MessageFileTypeUnknown

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class GetMessageFileType(Function[MessageFileTypePrivate | MessageFileTypeGroup | MessageFileTypeUnknown]):
    """
    Returns information about a file with messages exported from another application

    :param message_file_head: Beginning of the message file; up to 100 first lines
    :return: :class:`MessageFileTypePrivate | MessageFileTypeGroup | MessageFileTypeUnknown`
    """
    __slots__ = ("message_file_head", "_extra", "_client_id", "_type")

    def __init__(self, message_file_head: str = ""):
        self.message_file_head = message_file_head
        self._type = "getMessageFileType"