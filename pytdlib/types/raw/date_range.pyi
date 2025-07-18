from .object_base import ObjectBase

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class DateRange(ObjectBase):
    """
    Represents a date range

    :param start_date: Point in time (Unix timestamp) at which the date range begins
    :param end_date: Point in time (Unix timestamp) at which the date range ends
    """
    __slots__ = ("start_date", "end_date", "_extra", "_client_id", "_type")

    def __init__(self, start_date: int = 0, end_date: int = 0):
        self.start_date = start_date
        self.end_date = end_date
        self._type = "dateRange"