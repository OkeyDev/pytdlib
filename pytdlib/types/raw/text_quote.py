from .object_base import ObjectBase

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class TextQuote(ObjectBase):
    """
    Describes manually or automatically chosen quote from another message

    :param text: Text of the quote. Only Bold, Italic, Underline, Strikethrough, Spoiler, and CustomEmoji entities can be present in the text
    :param position: Approximate quote position in the original message in UTF-16 code units as specified by the message sender
    :param is_manual: True, if the quote was manually chosen by the message sender
    """
    __slots__ = ("text", "position", "is_manual", "_extra", "_client_id", "_type")

    def __init__(self, text = None, position = None, is_manual = None):
        self.text = text
        self.position = position
        self.is_manual = is_manual
        self._type = "textQuote"