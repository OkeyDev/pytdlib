from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class GetMarkdownText(Function):
    """
    Replaces text entities with Markdown formatting in a human-friendly format. Entities that can't be represented in Markdown unambiguously are kept as is. Can be called synchronously

    :param text: The text
    :return: :class:`FormattedText`
    """
    __slots__ = ("text", "_extra", "_client_id", "_type")

    def __init__(self, text = None):
        self.text = text
        self._type = "getMarkdownText"