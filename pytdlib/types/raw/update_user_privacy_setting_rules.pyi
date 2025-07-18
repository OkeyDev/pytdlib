from .update import Update
from .user_privacy_setting import UserPrivacySetting
from .user_privacy_setting_rules import UserPrivacySettingRules

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class UpdateUserPrivacySettingRules(Update):
    """
    Some privacy setting rules have been changed

    :param setting: The privacy setting
    :param rules: New privacy rules
    """
    __slots__ = ("setting", "rules", "_extra", "_client_id", "_type")

    def __init__(self, setting: UserPrivacySetting | None = None, rules: UserPrivacySettingRules | None = None):
        self.setting = setting
        self.rules = rules
        self._type = "updateUserPrivacySettingRules"