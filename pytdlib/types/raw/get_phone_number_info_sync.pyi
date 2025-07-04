from .function import Function

from .phone_number_info import PhoneNumberInfo

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class GetPhoneNumberInfoSync(Function[PhoneNumberInfo]):
    """
    Returns information about a phone number by its prefix synchronously. getCountries must be called at least once after changing localization to the specified language if properly localized country information is expected. Can be called synchronously

    :param language_code: A two-letter ISO 639-1 language code for country information localization
    :param phone_number_prefix: The phone number prefix
    :return: :class:`PhoneNumberInfo`
    """
    __slots__ = ("language_code", "phone_number_prefix", "_extra", "_client_id", "_type")

    def __init__(self, language_code: str = "", phone_number_prefix: str = ""):
        self.language_code = language_code
        self.phone_number_prefix = phone_number_prefix
        self._type = "getPhoneNumberInfoSync"