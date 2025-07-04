from .message_effect_type import MessageEffectType
from .object_base import ObjectBase
from .sticker import Sticker

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class MessageEffect(ObjectBase):
    """
    Contains information about an effect added to a message

    :param id: Unique identifier of the effect
    :param static_icon: Static icon for the effect in WEBP format; may be null if none
    :param emoji: Emoji corresponding to the effect that can be used if static icon isn't available
    :param is_premium: True, if Telegram Premium subscription is required to use the effect
    :param type: Type of the effect
    """
    __slots__ = ("id", "static_icon", "emoji", "is_premium", "type", "_extra", "_client_id", "_type")

    def __init__(self, id: int = 0, static_icon: Sticker | None = None, emoji: str = "", is_premium: bool = False, type: MessageEffectType | None = None):
        self.id = id
        self.static_icon = static_icon
        self.emoji = emoji
        self.is_premium = is_premium
        self.type = type
        self._type = "messageEffect"