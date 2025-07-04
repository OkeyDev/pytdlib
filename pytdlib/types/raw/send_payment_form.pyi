from .function import Function

from .input_credentials import InputCredentials
from .input_invoice import InputInvoice
from .payment_result import PaymentResult

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class SendPaymentForm(Function[PaymentResult]):
    """
    Sends a filled-out payment form to the bot for final verification

    :param input_invoice: The invoice
    :param payment_form_id: Payment form identifier returned by getPaymentForm
    :param order_info_id: Identifier returned by validateOrderInfo, or an empty string
    :param shipping_option_id: Identifier of a chosen shipping option, if applicable
    :param credentials: The credentials chosen by user for payment; pass null for a payment in Telegram Stars
    :param tip_amount: Chosen by the user amount of tip in the smallest units of the currency
    :return: :class:`PaymentResult`
    """
    __slots__ = ("input_invoice", "payment_form_id", "order_info_id", "shipping_option_id", "credentials", "tip_amount", "_extra", "_client_id", "_type")

    def __init__(self, input_invoice: InputInvoice | None = None, payment_form_id: int = 0, order_info_id: str = "", shipping_option_id: str = "", credentials: InputCredentials | None = None, tip_amount: int = 0):
        self.input_invoice = input_invoice
        self.payment_form_id = payment_form_id
        self.order_info_id = order_info_id
        self.shipping_option_id = shipping_option_id
        self.credentials = credentials
        self.tip_amount = tip_amount
        self._type = "sendPaymentForm"