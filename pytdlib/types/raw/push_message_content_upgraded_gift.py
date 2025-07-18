from .push_message_content import PushMessageContent

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class PushMessageContentUpgradedGift(PushMessageContent):
    """
    A message with an upgraded gift

    :param is_upgrade: True, if the gift was obtained by upgrading of a previously received gift; otherwise, this is a transferred or resold gift
    """
    __slots__ = ("is_upgrade", "_extra", "_client_id", "_type")

    def __init__(self, is_upgrade = None):
        self.is_upgrade = is_upgrade
        self._type = "pushMessageContentUpgradedGift"