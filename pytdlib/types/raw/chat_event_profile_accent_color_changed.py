from .chat_event_action import ChatEventAction

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class ChatEventProfileAccentColorChanged(ChatEventAction):
    """
    The chat's profile accent color or profile background custom emoji were changed

    :param old_profile_accent_color_id: Previous identifier of chat's profile accent color; -1 if none
    :param old_profile_background_custom_emoji_id: Previous identifier of the custom emoji; 0 if none
    :param new_profile_accent_color_id: New identifier of chat's profile accent color; -1 if none
    :param new_profile_background_custom_emoji_id: New identifier of the custom emoji; 0 if none
    """
    __slots__ = ("old_profile_accent_color_id", "old_profile_background_custom_emoji_id", "new_profile_accent_color_id", "new_profile_background_custom_emoji_id", "_extra", "_client_id", "_type")

    def __init__(self, old_profile_accent_color_id = None, old_profile_background_custom_emoji_id = None, new_profile_accent_color_id = None, new_profile_background_custom_emoji_id = None):
        self.old_profile_accent_color_id = old_profile_accent_color_id
        self.old_profile_background_custom_emoji_id = old_profile_background_custom_emoji_id
        self.new_profile_accent_color_id = new_profile_accent_color_id
        self.new_profile_background_custom_emoji_id = new_profile_background_custom_emoji_id
        self._type = "chatEventProfileAccentColorChanged"