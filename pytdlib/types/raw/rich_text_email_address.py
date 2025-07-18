from .rich_text import RichText

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class RichTextEmailAddress(RichText):
    """
    A rich text email link

    :param text: Text
    :param email_address: Email address
    """
    __slots__ = ("text", "email_address", "_extra", "_client_id", "_type")

    def __init__(self, text = None, email_address = None):
        self.text = text
        self.email_address = email_address
        self._type = "richTextEmailAddress"