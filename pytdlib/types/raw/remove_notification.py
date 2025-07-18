from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class RemoveNotification(Function):
    """
    Removes an active notification from notification list. Needs to be called only if the notification is removed by the current user

    :param notification_group_id: Identifier of notification group to which the notification belongs
    :param notification_id: Identifier of removed notification
    :return: :class:`Ok`
    """
    __slots__ = ("notification_group_id", "notification_id", "_extra", "_client_id", "_type")

    def __init__(self, notification_group_id = None, notification_id = None):
        self.notification_group_id = notification_group_id
        self.notification_id = notification_id
        self._type = "removeNotification"