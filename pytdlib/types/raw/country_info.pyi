from .object_base import ObjectBase
from typing import List

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class CountryInfo(ObjectBase):
    """
    Contains information about a country

    :param country_code: A two-letter ISO 3166-1 alpha-2 country code
    :param name: Native name of the country
    :param english_name: English name of the country
    :param is_hidden: True, if the country must be hidden from the list of all countries
    :param calling_codes: List of country calling codes
    """
    __slots__ = ("country_code", "name", "english_name", "is_hidden", "calling_codes", "_extra", "_client_id", "_type")

    def __init__(self, country_code: str = "", name: str = "", english_name: str = "", is_hidden: bool = False, calling_codes: List[str] | None = None):
        self.country_code = country_code
        self.name = name
        self.english_name = english_name
        self.is_hidden = is_hidden
        self.calling_codes = calling_codes
        self._type = "countryInfo"