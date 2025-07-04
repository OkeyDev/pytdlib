from .object_base import ObjectBase

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class NetworkStatistics(ObjectBase):
    """
    A full list of available network statistic entries

    :param since_date: Point in time (Unix timestamp) from which the statistics are collected
    :param entries: Network statistics entries
    """
    __slots__ = ("since_date", "entries", "_extra", "_client_id", "_type")

    def __init__(self, since_date = None, entries = None):
        self.since_date = since_date
        self.entries = entries
        self._type = "networkStatistics"