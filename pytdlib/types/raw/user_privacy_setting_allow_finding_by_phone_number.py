from .user_privacy_setting import UserPrivacySetting

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class UserPrivacySettingAllowFindingByPhoneNumber(UserPrivacySetting):
    """
    A privacy setting for managing whether the user can be found by their phone number. Checked only if the phone number is not known to the other user. Can be set only to "Allow contacts" or "Allow all"

    """
    __slots__ = ("_extra", "_client_id", "_type")

    def __init__(self):

        self._type = "userPrivacySettingAllowFindingByPhoneNumber"