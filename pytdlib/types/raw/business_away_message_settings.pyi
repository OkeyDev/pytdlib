from .business_away_message_schedule import BusinessAwayMessageSchedule
from .business_recipients import BusinessRecipients
from .object_base import ObjectBase

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class BusinessAwayMessageSettings(ObjectBase):
    """
    Describes settings for messages that are automatically sent by a Telegram Business account when it is away

    :param shortcut_id: Unique quick reply shortcut identifier for the away messages
    :param recipients: Chosen recipients of the away messages
    :param schedule: Settings used to check whether the current user is away
    :param offline_only: True, if the messages must not be sent if the account was online in the last 10 minutes
    """
    __slots__ = ("shortcut_id", "recipients", "schedule", "offline_only", "_extra", "_client_id", "_type")

    def __init__(self, shortcut_id: int = 0, recipients: BusinessRecipients | None = None, schedule: BusinessAwayMessageSchedule | None = None, offline_only: bool = False):
        self.shortcut_id = shortcut_id
        self.recipients = recipients
        self.schedule = schedule
        self.offline_only = offline_only
        self._type = "businessAwayMessageSettings"