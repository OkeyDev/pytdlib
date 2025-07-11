from .internal_link_type import InternalLinkType

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class InternalLinkTypePremiumFeatures(InternalLinkType):
    """
    The link is a link to the Premium features screen of the application from which the user can subscribe to Telegram Premium. Call getPremiumFeatures with the given referrer to process the link

    :param referrer: Referrer specified in the link
    """
    __slots__ = ("referrer", "_extra", "_client_id", "_type")

    def __init__(self, referrer = None):
        self.referrer = referrer
        self._type = "internalLinkTypePremiumFeatures"