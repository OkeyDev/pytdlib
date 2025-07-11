from .update import Update

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class UpdateUserPrivacySettingRules(Update):
    """
    Some privacy setting rules have been changed

    :param setting: The privacy setting
    :param rules: New privacy rules
    """
    __slots__ = ("setting", "rules", "_extra", "_client_id", "_type")

    def __init__(self, setting = None, rules = None):
        self.setting = setting
        self.rules = rules
        self._type = "updateUserPrivacySettingRules"