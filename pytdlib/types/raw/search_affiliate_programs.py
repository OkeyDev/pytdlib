from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class SearchAffiliatePrograms(Function):
    """
    Searches affiliate programs that can be connected to the given affiliate

    :param affiliate: The affiliate for which affiliate programs are searched for
    :param sort_order: Sort order for the results
    :param offset: Offset of the first affiliate program to return as received from the previous request; use empty string to get the first chunk of results
    :param limit: The maximum number of affiliate programs to return
    :return: :class:`FoundAffiliatePrograms`
    """
    __slots__ = ("affiliate", "sort_order", "offset", "limit", "_extra", "_client_id", "_type")

    def __init__(self, affiliate = None, sort_order = None, offset = None, limit = None):
        self.affiliate = affiliate
        self.sort_order = sort_order
        self.offset = offset
        self.limit = limit
        self._type = "searchAffiliatePrograms"