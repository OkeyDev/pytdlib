from .encrypted_credentials import EncryptedCredentials
from .encrypted_passport_element import EncryptedPassportElement
from .message_content import MessageContent
from typing import List

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class MessagePassportDataReceived(MessageContent):
    """
    Telegram Passport data has been received; for bots only

    :param elements: List of received Telegram Passport elements
    :param credentials: Encrypted data credentials
    """
    __slots__ = ("elements", "credentials", "_extra", "_client_id", "_type")

    def __init__(self, elements: List[EncryptedPassportElement] | None = None, credentials: EncryptedCredentials | None = None):
        self.elements = elements
        self.credentials = credentials
        self._type = "messagePassportDataReceived"