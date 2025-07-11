from .object_base import ObjectBase

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class BusinessOpeningHoursInterval(ObjectBase):
    """
    Describes an interval of time when the business is open

    :param start_minute: The minute's sequence number in a week, starting on Monday, marking the start of the time interval during which the business is open; 0-7*24*60
    :param end_minute: The minute's sequence number in a week, starting on Monday, marking the end of the time interval during which the business is open; 1-8*24*60
    """
    __slots__ = ("start_minute", "end_minute", "_extra", "_client_id", "_type")

    def __init__(self, start_minute = None, end_minute = None):
        self.start_minute = start_minute
        self.end_minute = end_minute
        self._type = "businessOpeningHoursInterval"