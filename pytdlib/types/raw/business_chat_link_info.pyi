from .formatted_text import FormattedText
from .object_base import ObjectBase

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class BusinessChatLinkInfo(ObjectBase):
    """
    Contains information about a business chat link

    :param chat_id: Identifier of the private chat that created the link
    :param text: Message draft text that must be added to the input field
    """
    __slots__ = ("chat_id", "text", "_extra", "_client_id", "_type")

    def __init__(self, chat_id: int = 0, text: FormattedText | None = None):
        self.chat_id = chat_id
        self.text = text
        self._type = "businessChatLinkInfo"