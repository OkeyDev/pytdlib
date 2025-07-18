from .background import Background
from .background_fill import BackgroundFill
from .object_base import ObjectBase

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class ThemeSettings(ObjectBase):
    """
    Describes theme settings

    :param accent_color: Theme accent color in ARGB format
    :param background: The background to be used in chats; may be null
    :param outgoing_message_fill: The fill to be used as a background for outgoing messages
    :param animate_outgoing_message_fill: If true, the freeform gradient fill needs to be animated on every sent message
    :param outgoing_message_accent_color: Accent color of outgoing messages in ARGB format
    """
    __slots__ = ("accent_color", "background", "outgoing_message_fill", "animate_outgoing_message_fill", "outgoing_message_accent_color", "_extra", "_client_id", "_type")

    def __init__(self, accent_color: int = 0, background: Background | None = None, outgoing_message_fill: BackgroundFill | None = None, animate_outgoing_message_fill: bool = False, outgoing_message_accent_color: int = 0):
        self.accent_color = accent_color
        self.background = background
        self.outgoing_message_fill = outgoing_message_fill
        self.animate_outgoing_message_fill = animate_outgoing_message_fill
        self.outgoing_message_accent_color = outgoing_message_accent_color
        self._type = "themeSettings"