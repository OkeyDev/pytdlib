from .object_base import ObjectBase

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class ChatTheme(ObjectBase):
    """
    Describes a chat theme

    :param name: Theme name
    :param light_settings: Theme settings for a light chat theme
    :param dark_settings: Theme settings for a dark chat theme
    """
    __slots__ = ("name", "light_settings", "dark_settings", "_extra", "_client_id", "_type")

    def __init__(self, name = None, light_settings = None, dark_settings = None):
        self.name = name
        self.light_settings = light_settings
        self.dark_settings = dark_settings
        self._type = "chatTheme"