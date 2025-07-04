from .object_base import ObjectBase

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class CallbackQueryAnswer(ObjectBase):
    """
    Contains a bot's answer to a callback query

    :param text: Text of the answer
    :param show_alert: True, if an alert must be shown to the user instead of a toast notification
    :param url: URL to be opened
    """
    __slots__ = ("text", "show_alert", "url", "_extra", "_client_id", "_type")

    def __init__(self, text = None, show_alert = None, url = None):
        self.text = text
        self.show_alert = show_alert
        self.url = url
        self._type = "callbackQueryAnswer"