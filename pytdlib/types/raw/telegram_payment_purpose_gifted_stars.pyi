from .telegram_payment_purpose import TelegramPaymentPurpose

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class TelegramPaymentPurposeGiftedStars(TelegramPaymentPurpose):
    """
    The user buying Telegram Stars for other users

    :param user_id: Identifier of the user to which Telegram Stars are gifted
    :param currency: ISO 4217 currency code of the payment currency
    :param amount: Paid amount, in the smallest units of the currency
    :param star_count: Number of bought Telegram Stars
    """
    __slots__ = ("user_id", "currency", "amount", "star_count", "_extra", "_client_id", "_type")

    def __init__(self, user_id: int = 0, currency: str = "", amount: int = 0, star_count: int = 0):
        self.user_id = user_id
        self.currency = currency
        self.amount = amount
        self.star_count = star_count
        self._type = "telegramPaymentPurposeGiftedStars"