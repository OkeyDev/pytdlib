from .authorization_state import AuthorizationState

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class AuthorizationStateWaitPremiumPurchase(AuthorizationState):
    """
    The user must buy Telegram Premium as an in-store purchase to log in. Call checkAuthenticationPremiumPurchase and then setAuthenticationPremiumPurchaseTransaction

    :param store_product_id: Identifier of the store product that must be bought
    """
    __slots__ = ("store_product_id", "_extra", "_client_id", "_type")

    def __init__(self, store_product_id = None):
        self.store_product_id = store_product_id
        self._type = "authorizationStateWaitPremiumPurchase"