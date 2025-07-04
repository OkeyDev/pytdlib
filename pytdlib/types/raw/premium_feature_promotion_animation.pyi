from .animation import Animation
from .object_base import ObjectBase
from .premium_feature import PremiumFeature

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class PremiumFeaturePromotionAnimation(ObjectBase):
    """
    Describes a promotion animation for a Premium feature

    :param feature: Premium feature
    :param animation: Promotion animation for the feature
    """
    __slots__ = ("feature", "animation", "_extra", "_client_id", "_type")

    def __init__(self, feature: PremiumFeature | None = None, animation: Animation | None = None):
        self.feature = feature
        self.animation = animation
        self._type = "premiumFeaturePromotionAnimation"