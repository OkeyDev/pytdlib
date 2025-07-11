from .inline_keyboard_button_type import InlineKeyboardButtonType

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class InlineKeyboardButtonTypeWebApp(InlineKeyboardButtonType):
    """
    A button that opens a Web App by calling openWebApp

    :param url: An HTTP URL to pass to openWebApp
    """
    __slots__ = ("url", "_extra", "_client_id", "_type")

    def __init__(self, url = None):
        self.url = url
        self._type = "inlineKeyboardButtonTypeWebApp"