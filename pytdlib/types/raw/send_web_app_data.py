from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class SendWebAppData(Function):
    """
    Sends data received from a keyboardButtonTypeWebApp Web App to a bot

    :param bot_user_id: Identifier of the target bot
    :param button_text: Text of the keyboardButtonTypeWebApp button, which opened the Web App
    :param data: The data
    :return: :class:`Ok`
    """
    __slots__ = ("bot_user_id", "button_text", "data", "_extra", "_client_id", "_type")

    def __init__(self, bot_user_id = None, button_text = None, data = None):
        self.bot_user_id = bot_user_id
        self.button_text = button_text
        self.data = data
        self._type = "sendWebAppData"