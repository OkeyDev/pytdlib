from .function import Function

from .countries import Countries

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class GetCountries(Function[Countries]):
    """
    Returns information about existing countries. Can be called before authorization

    :return: :class:`Countries`
    """
    __slots__ = ("_extra", "_client_id", "_type")

    def __init__(self):

        self._type = "getCountries"