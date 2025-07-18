from .object_base import ObjectBase

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class BusinessGreetingMessageSettings(ObjectBase):
    """
    Describes settings for greeting messages that are automatically sent by a Telegram Business account as response to incoming messages in an inactive private chat

    :param shortcut_id: Unique quick reply shortcut identifier for the greeting messages
    :param recipients: Chosen recipients of the greeting messages
    :param inactivity_days: The number of days after which a chat will be considered as inactive; currently, must be on of 7, 14, 21, or 28
    """
    __slots__ = ("shortcut_id", "recipients", "inactivity_days", "_extra", "_client_id", "_type")

    def __init__(self, shortcut_id = None, recipients = None, inactivity_days = None):
        self.shortcut_id = shortcut_id
        self.recipients = recipients
        self.inactivity_days = inactivity_days
        self._type = "businessGreetingMessageSettings"