from .function import Function

from .ok import Ok

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class ClickPremiumSubscriptionButton(Function[Ok]):
    """
    Informs TDLib that the user clicked Premium subscription button on the Premium features screen

    :return: :class:`Ok`
    """
    __slots__ = ("_extra", "_client_id", "_type")

    def __init__(self):

        self._type = "clickPremiumSubscriptionButton"