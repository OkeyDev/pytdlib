from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class GetPhoneNumberInfo(Function):
    """
    Returns information about a phone number by its prefix. Can be called before authorization

    :param phone_number_prefix: The phone number prefix
    :return: :class:`PhoneNumberInfo`
    """
    __slots__ = ("phone_number_prefix", "_extra", "_client_id", "_type")

    def __init__(self, phone_number_prefix = None):
        self.phone_number_prefix = phone_number_prefix
        self._type = "getPhoneNumberInfo"