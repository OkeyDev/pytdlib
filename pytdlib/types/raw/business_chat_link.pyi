from .formatted_text import FormattedText
from .object_base import ObjectBase

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class BusinessChatLink(ObjectBase):
    """
    Contains information about a business chat link

    :param link: The HTTPS link
    :param text: Message draft text that will be added to the input field
    :param title: Link title
    :param view_count: Number of times the link was used
    """
    __slots__ = ("link", "text", "title", "view_count", "_extra", "_client_id", "_type")

    def __init__(self, link: str = "", text: FormattedText | None = None, title: str = "", view_count: int = 0):
        self.link = link
        self.text = text
        self.title = title
        self.view_count = view_count
        self._type = "businessChatLink"