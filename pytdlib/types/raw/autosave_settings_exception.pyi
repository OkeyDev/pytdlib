from .object_base import ObjectBase
from .scope_autosave_settings import ScopeAutosaveSettings

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class AutosaveSettingsException(ObjectBase):
    """
    Contains autosave settings for a chat, which overrides default settings for the corresponding scope

    :param chat_id: Chat identifier
    :param settings: Autosave settings for the chat
    """
    __slots__ = ("chat_id", "settings", "_extra", "_client_id", "_type")

    def __init__(self, chat_id: int = 0, settings: ScopeAutosaveSettings | None = None):
        self.chat_id = chat_id
        self.settings = settings
        self._type = "autosaveSettingsException"