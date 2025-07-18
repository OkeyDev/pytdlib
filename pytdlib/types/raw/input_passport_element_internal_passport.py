from .input_passport_element import InputPassportElement

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class InputPassportElementInternalPassport(InputPassportElement):
    """
    A Telegram Passport element to be saved containing the user's internal passport

    :param internal_passport: The internal passport to be saved
    """
    __slots__ = ("internal_passport", "_extra", "_client_id", "_type")

    def __init__(self, internal_passport = None):
        self.internal_passport = internal_passport
        self._type = "inputPassportElementInternalPassport"