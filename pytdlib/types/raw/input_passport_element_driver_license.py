from .input_passport_element import InputPassportElement

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class InputPassportElementDriverLicense(InputPassportElement):
    """
    A Telegram Passport element to be saved containing the user's driver license

    :param driver_license: The driver license to be saved
    """
    __slots__ = ("driver_license", "_extra", "_client_id", "_type")

    def __init__(self, driver_license = None):
        self.driver_license = driver_license
        self._type = "inputPassportElementDriverLicense"