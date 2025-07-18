from .object_base import ObjectBase

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class ChatBoostFeatures(ObjectBase):
    """
    Contains a list of features available on the first chat boost levels

    :param features: The list of features
    :param min_profile_background_custom_emoji_boost_level: The minimum boost level required to set custom emoji for profile background
    :param min_background_custom_emoji_boost_level: The minimum boost level required to set custom emoji for reply header and link preview background; for channel chats only
    :param min_emoji_status_boost_level: The minimum boost level required to set emoji status
    :param min_chat_theme_background_boost_level: The minimum boost level required to set a chat theme background as chat background
    :param min_custom_background_boost_level: The minimum boost level required to set custom chat background
    :param min_custom_emoji_sticker_set_boost_level: The minimum boost level required to set custom emoji sticker set for the chat; for supergroup chats only
    :param min_automatic_translation_boost_level: The minimum boost level allowing to enable automatic translation of messages for non-Premium users; for channel chats only
    :param min_speech_recognition_boost_level: The minimum boost level allowing to recognize speech in video note and voice note messages for non-Premium users; for supergroup chats only
    :param min_sponsored_message_disable_boost_level: The minimum boost level allowing to disable sponsored messages in the chat; for channel chats only
    """
    __slots__ = ("features", "min_profile_background_custom_emoji_boost_level", "min_background_custom_emoji_boost_level", "min_emoji_status_boost_level", "min_chat_theme_background_boost_level", "min_custom_background_boost_level", "min_custom_emoji_sticker_set_boost_level", "min_automatic_translation_boost_level", "min_speech_recognition_boost_level", "min_sponsored_message_disable_boost_level", "_extra", "_client_id", "_type")

    def __init__(self, features = None, min_profile_background_custom_emoji_boost_level = None, min_background_custom_emoji_boost_level = None, min_emoji_status_boost_level = None, min_chat_theme_background_boost_level = None, min_custom_background_boost_level = None, min_custom_emoji_sticker_set_boost_level = None, min_automatic_translation_boost_level = None, min_speech_recognition_boost_level = None, min_sponsored_message_disable_boost_level = None):
        self.features = features
        self.min_profile_background_custom_emoji_boost_level = min_profile_background_custom_emoji_boost_level
        self.min_background_custom_emoji_boost_level = min_background_custom_emoji_boost_level
        self.min_emoji_status_boost_level = min_emoji_status_boost_level
        self.min_chat_theme_background_boost_level = min_chat_theme_background_boost_level
        self.min_custom_background_boost_level = min_custom_background_boost_level
        self.min_custom_emoji_sticker_set_boost_level = min_custom_emoji_sticker_set_boost_level
        self.min_automatic_translation_boost_level = min_automatic_translation_boost_level
        self.min_speech_recognition_boost_level = min_speech_recognition_boost_level
        self.min_sponsored_message_disable_boost_level = min_sponsored_message_disable_boost_level
        self._type = "chatBoostFeatures"