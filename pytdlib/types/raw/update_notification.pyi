from .notification import Notification
from .update import Update

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class UpdateNotification(Update):
    """
    A notification was changed

    :param notification_group_id: Unique notification group identifier
    :param notification: Changed notification
    """
    __slots__ = ("notification_group_id", "notification", "_extra", "_client_id", "_type")

    def __init__(self, notification_group_id: int = 0, notification: Notification | None = None):
        self.notification_group_id = notification_group_id
        self.notification = notification
        self._type = "updateNotification"