from .push_message_content import PushMessageContent

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class PushMessageContentHidden(PushMessageContent):
    """
    A general message with hidden content

    :param is_pinned: True, if the message is a pinned message with the specified content
    """
    __slots__ = ("is_pinned", "_extra", "_client_id", "_type")

    def __init__(self, is_pinned = None):
        self.is_pinned = is_pinned
        self._type = "pushMessageContentHidden"