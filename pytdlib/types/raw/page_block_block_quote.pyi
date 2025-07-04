from .page_block import PageBlock
from .rich_text import RichText

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class PageBlockBlockQuote(PageBlock):
    """
    A block quote

    :param text: Quote text
    :param credit: Quote credit
    """
    __slots__ = ("text", "credit", "_extra", "_client_id", "_type")

    def __init__(self, text: RichText | None = None, credit: RichText | None = None):
        self.text = text
        self.credit = credit
        self._type = "pageBlockBlockQuote"