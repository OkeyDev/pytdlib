from .page_block import PageBlock

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class PageBlockTitle(PageBlock):
    """
    The title of a page

    :param title: Title
    """
    __slots__ = ("title", "_extra", "_client_id", "_type")

    def __init__(self, title = None):
        self.title = title
        self._type = "pageBlockTitle"