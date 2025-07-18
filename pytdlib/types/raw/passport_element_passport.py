from .passport_element import PassportElement

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class PassportElementPassport(PassportElement):
    """
    A Telegram Passport element containing the user's passport

    :param passport: Passport
    """
    __slots__ = ("passport", "_extra", "_client_id", "_type")

    def __init__(self, passport = None):
        self.passport = passport
        self._type = "passportElementPassport"