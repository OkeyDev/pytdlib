from .country_info import CountryInfo
from .object_base import ObjectBase
from typing import List

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class Countries(ObjectBase):
    """
    Contains information about countries

    :param countries: The list of countries
    """
    __slots__ = ("countries", "_extra", "_client_id", "_type")

    def __init__(self, countries: List[CountryInfo] | None = None):
        self.countries = countries
        self._type = "countries"