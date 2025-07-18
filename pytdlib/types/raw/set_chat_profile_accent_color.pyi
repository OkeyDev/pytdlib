from .function import Function

from .ok import Ok

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class SetChatProfileAccentColor(Function[Ok]):
    """
    Changes accent color and background custom emoji for profile of a supergroup or channel chat. Requires can_change_info administrator right

    :param chat_id: Chat identifier
    :param profile_accent_color_id: Identifier of the accent color to use for profile; pass -1 if none. The chat must have at least profileAccentColor.min_supergroup_chat_boost_level for supergroups or profileAccentColor.min_channel_chat_boost_level for channels boost level to pass the corresponding color
    :param profile_background_custom_emoji_id: Identifier of a custom emoji to be shown on the chat's profile photo background; 0 if none. Use chatBoostLevelFeatures.can_set_profile_background_custom_emoji to check whether a custom emoji can be set
    :return: :class:`Ok`
    """
    __slots__ = ("chat_id", "profile_accent_color_id", "profile_background_custom_emoji_id", "_extra", "_client_id", "_type")

    def __init__(self, chat_id: int = 0, profile_accent_color_id: int = 0, profile_background_custom_emoji_id: int = 0):
        self.chat_id = chat_id
        self.profile_accent_color_id = profile_accent_color_id
        self.profile_background_custom_emoji_id = profile_background_custom_emoji_id
        self._type = "setChatProfileAccentColor"