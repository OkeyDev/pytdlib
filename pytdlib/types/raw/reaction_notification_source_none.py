from .reaction_notification_source import ReactionNotificationSource

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class ReactionNotificationSourceNone(ReactionNotificationSource):
    """
    Notifications for reactions are disabled

    """
    __slots__ = ("_extra", "_client_id", "_type")

    def __init__(self):

        self._type = "reactionNotificationSourceNone"