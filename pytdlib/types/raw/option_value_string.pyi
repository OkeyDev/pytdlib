from .option_value import OptionValue

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class OptionValueString(OptionValue):
    """
    Represents a string option

    :param value: The value of the option
    """
    __slots__ = ("value", "_extra", "_client_id", "_type")

    def __init__(self, value: str = ""):
        self.value = value
        self._type = "optionValueString"