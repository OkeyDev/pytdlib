from .report_option import ReportOption
from .report_sponsored_result import ReportSponsoredResult
from typing import List

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class ReportSponsoredResultOptionRequired(ReportSponsoredResult):
    """
    The user must choose an option to report the message and repeat request with the chosen option

    :param title: Title for the option choice
    :param options: List of available options
    """
    __slots__ = ("title", "options", "_extra", "_client_id", "_type")

    def __init__(self, title: str = "", options: List[ReportOption] | None = None):
        self.title = title
        self.options = options
        self._type = "reportSponsoredResultOptionRequired"