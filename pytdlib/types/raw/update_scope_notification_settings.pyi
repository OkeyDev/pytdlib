from .notification_settings_scope import NotificationSettingsScope
from .scope_notification_settings import ScopeNotificationSettings
from .update import Update

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class UpdateScopeNotificationSettings(Update):
    """
    Notification settings for some type of chats were updated

    :param scope: Types of chats for which notification settings were updated
    :param notification_settings: The new notification settings
    """
    __slots__ = ("scope", "notification_settings", "_extra", "_client_id", "_type")

    def __init__(self, scope: NotificationSettingsScope | None = None, notification_settings: ScopeNotificationSettings | None = None):
        self.scope = scope
        self.notification_settings = notification_settings
        self._type = "updateScopeNotificationSettings"