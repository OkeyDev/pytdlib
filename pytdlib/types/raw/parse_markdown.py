from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class ParseMarkdown(Function):
    """
    Parses Markdown entities in a human-friendly format, ignoring markup errors. Can be called synchronously

    :param text: The text to parse. For example, "__italic__ ~~strikethrough~~ ||spoiler|| **bold** `code` ```pre``` __[italic__ text_url](telegram.org) __italic**bold italic__bold**"
    :return: :class:`FormattedText`
    """
    __slots__ = ("text", "_extra", "_client_id", "_type")

    def __init__(self, text = None):
        self.text = text
        self._type = "parseMarkdown"