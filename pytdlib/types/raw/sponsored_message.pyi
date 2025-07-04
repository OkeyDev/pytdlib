from .message_content import MessageContent
from .message_sponsor import MessageSponsor
from .object_base import ObjectBase

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class SponsoredMessage(ObjectBase):
    """
    Describes a sponsored message

    :param message_id: Message identifier; unique for the chat to which the sponsored message belongs among both ordinary and sponsored messages
    :param is_recommended: True, if the message needs to be labeled as "recommended" instead of "sponsored"
    :param can_be_reported: True, if the message can be reported to Telegram moderators through reportChatSponsoredMessage
    :param content: Content of the message. Currently, can be only of the types messageText, messageAnimation, messagePhoto, or messageVideo. Video messages can be viewed fullscreen
    :param sponsor: Information about the sponsor of the message
    :param title: Title of the sponsored message
    :param button_text: Text for the message action button
    :param accent_color_id: Identifier of the accent color for title, button text and message background
    :param background_custom_emoji_id: Identifier of a custom emoji to be shown on the message background; 0 if none
    :param additional_info: If non-empty, additional information about the sponsored message to be shown along with the message
    """
    __slots__ = ("message_id", "is_recommended", "can_be_reported", "content", "sponsor", "title", "button_text", "accent_color_id", "background_custom_emoji_id", "additional_info", "_extra", "_client_id", "_type")

    def __init__(self, message_id: int = 0, is_recommended: bool = False, can_be_reported: bool = False, content: MessageContent | None = None, sponsor: MessageSponsor | None = None, title: str = "", button_text: str = "", accent_color_id: int = 0, background_custom_emoji_id: int = 0, additional_info: str = ""):
        self.message_id = message_id
        self.is_recommended = is_recommended
        self.can_be_reported = can_be_reported
        self.content = content
        self.sponsor = sponsor
        self.title = title
        self.button_text = button_text
        self.accent_color_id = accent_color_id
        self.background_custom_emoji_id = background_custom_emoji_id
        self.additional_info = additional_info
        self._type = "sponsoredMessage"