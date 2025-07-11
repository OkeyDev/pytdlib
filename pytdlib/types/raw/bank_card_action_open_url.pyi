from .object_base import ObjectBase

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class BankCardActionOpenUrl(ObjectBase):
    """
    Describes an action associated with a bank card number

    :param text: Action text
    :param url: The URL to be opened
    """
    __slots__ = ("text", "url", "_extra", "_client_id", "_type")

    def __init__(self, text: str = "", url: str = ""):
        self.text = text
        self.url = url
        self._type = "bankCardActionOpenUrl"