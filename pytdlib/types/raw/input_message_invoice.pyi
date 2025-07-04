from .formatted_text import FormattedText
from .input_message_content import InputMessageContent
from .input_paid_media import InputPaidMedia
from .invoice import Invoice

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class InputMessageInvoice(InputMessageContent):
    """
    A message with an invoice; can be used only by bots

    :param invoice: Invoice
    :param title: Product title; 1-32 characters
    :param description: A message with an invoice; can be used only by bots
    :param photo_url: Product photo URL; optional
    :param photo_size: Product photo size
    :param photo_width: Product photo width
    :param photo_height: Product photo height
    :param payload: The invoice payload
    :param provider_token: Payment provider token; may be empty for payments in Telegram Stars
    :param provider_data: JSON-encoded data about the invoice, which will be shared with the payment provider
    :param start_parameter: Unique invoice bot deep link parameter for the generation of this invoice. If empty, it would be possible to pay directly from forwards of the invoice message
    :param paid_media: The content of paid media attached to the invoice; pass null if none
    :param paid_media_caption: Paid media caption; pass null to use an empty caption; 0-getOption("message_caption_length_max") characters
    """
    __slots__ = ("invoice", "title", "description", "photo_url", "photo_size", "photo_width", "photo_height", "payload", "provider_token", "provider_data", "start_parameter", "paid_media", "paid_media_caption", "_extra", "_client_id", "_type")

    def __init__(self, invoice: Invoice | None = None, title: str = "", description: str = "", photo_url: str = "", photo_size: int = 0, photo_width: int = 0, photo_height: int = 0, payload: bytes = b"", provider_token: str = "", provider_data: str = "", start_parameter: str = "", paid_media: InputPaidMedia | None = None, paid_media_caption: FormattedText | None = None):
        self.invoice = invoice
        self.title = title
        self.description = description
        self.photo_url = photo_url
        self.photo_size = photo_size
        self.photo_width = photo_width
        self.photo_height = photo_height
        self.payload = payload
        self.provider_token = provider_token
        self.provider_data = provider_data
        self.start_parameter = start_parameter
        self.paid_media = paid_media
        self.paid_media_caption = paid_media_caption
        self._type = "inputMessageInvoice"