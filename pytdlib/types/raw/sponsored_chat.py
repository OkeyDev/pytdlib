from .object_base import ObjectBase

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class SponsoredChat(ObjectBase):
    """
    Describes a sponsored chat

    :param unique_id: Unique identifier of this result
    :param chat_id: Chat identifier
    :param sponsor_info: Additional optional information about the sponsor to be shown along with the chat
    :param additional_info: If non-empty, additional information about the sponsored chat to be shown along with the chat
    """
    __slots__ = ("unique_id", "chat_id", "sponsor_info", "additional_info", "_extra", "_client_id", "_type")

    def __init__(self, unique_id = None, chat_id = None, sponsor_info = None, additional_info = None):
        self.unique_id = unique_id
        self.chat_id = chat_id
        self.sponsor_info = sponsor_info
        self.additional_info = additional_info
        self._type = "sponsoredChat"