from .premium_feature import PremiumFeature

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class PremiumFeatureMessagePrivacy(PremiumFeature):
    """
    The ability to disallow incoming voice and video note messages in private chats using setUserPrivacySettingRules with userPrivacySettingAllowPrivateVoiceAndVideoNoteMessages and to restrict incoming messages from non-contacts using setNewChatPrivacySettings

    """
    __slots__ = ("_extra", "_client_id", "_type")

    def __init__(self):

        self._type = "premiumFeatureMessagePrivacy"