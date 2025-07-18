from .page_block import PageBlock

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class PageBlockEmbedded(PageBlock):
    """
    An embedded web page

    :param url: URL of the embedded page, if available
    :param html: HTML-markup of the embedded page
    :param poster_photo: Poster photo, if available; may be null
    :param width: Block width; 0 if unknown
    :param height: Block height; 0 if unknown
    :param caption: Block caption
    :param is_full_width: True, if the block must be full width
    :param allow_scrolling: True, if scrolling needs to be allowed
    """
    __slots__ = ("url", "html", "poster_photo", "width", "height", "caption", "is_full_width", "allow_scrolling", "_extra", "_client_id", "_type")

    def __init__(self, url = None, html = None, poster_photo = None, width = None, height = None, caption = None, is_full_width = None, allow_scrolling = None):
        self.url = url
        self.html = html
        self.poster_photo = poster_photo
        self.width = width
        self.height = height
        self.caption = caption
        self.is_full_width = is_full_width
        self.allow_scrolling = allow_scrolling
        self._type = "pageBlockEmbedded"