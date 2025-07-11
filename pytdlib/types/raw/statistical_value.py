from .object_base import ObjectBase

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class StatisticalValue(ObjectBase):
    """
    A value with information about its recent changes

    :param value: The current value
    :param previous_value: The value for the previous day
    :param growth_rate_percentage: The growth rate of the value, as a percentage
    """
    __slots__ = ("value", "previous_value", "growth_rate_percentage", "_extra", "_client_id", "_type")

    def __init__(self, value = None, previous_value = None, growth_rate_percentage = None):
        self.value = value
        self.previous_value = previous_value
        self.growth_rate_percentage = growth_rate_percentage
        self._type = "statisticalValue"