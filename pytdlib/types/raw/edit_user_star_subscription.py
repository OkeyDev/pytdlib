from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class EditUserStarSubscription(Function):
    """
    Cancels or re-enables Telegram Star subscription for a user; for bots only

    :param user_id: User identifier
    :param telegram_payment_charge_id: Telegram payment identifier of the subscription
    :param is_canceled: Pass true to cancel the subscription; pass false to allow the user to enable it
    :return: :class:`Ok`
    """
    __slots__ = ("user_id", "telegram_payment_charge_id", "is_canceled", "_extra", "_client_id", "_type")

    def __init__(self, user_id = None, telegram_payment_charge_id = None, is_canceled = None):
        self.user_id = user_id
        self.telegram_payment_charge_id = telegram_payment_charge_id
        self.is_canceled = is_canceled
        self._type = "editUserStarSubscription"