from .function import Function

from .report_sponsored_result_ads_hidden import ReportSponsoredResultAdsHidden
from .report_sponsored_result_failed import ReportSponsoredResultFailed
from .report_sponsored_result_ok import ReportSponsoredResultOk
from .report_sponsored_result_option_required import ReportSponsoredResultOptionRequired
from .report_sponsored_result_premium_required import ReportSponsoredResultPremiumRequired

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class ReportSponsoredChat(Function[ReportSponsoredResultOk | ReportSponsoredResultFailed | ReportSponsoredResultOptionRequired | ReportSponsoredResultAdsHidden | ReportSponsoredResultPremiumRequired]):
    """
    Reports a sponsored chat to Telegram moderators

    :param sponsored_chat_unique_id: Unique identifier of the sponsored chat
    :param option_id: Option identifier chosen by the user; leave empty for the initial request
    :return: :class:`ReportSponsoredResultOk | ReportSponsoredResultFailed | ReportSponsoredResultOptionRequired | ReportSponsoredResultAdsHidden | ReportSponsoredResultPremiumRequired`
    """
    __slots__ = ("sponsored_chat_unique_id", "option_id", "_extra", "_client_id", "_type")

    def __init__(self, sponsored_chat_unique_id: int = 0, option_id: bytes = b""):
        self.sponsored_chat_unique_id = sponsored_chat_unique_id
        self.option_id = option_id
        self._type = "reportSponsoredChat"