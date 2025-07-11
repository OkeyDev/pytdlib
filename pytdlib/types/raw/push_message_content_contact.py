from .push_message_content import PushMessageContent

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class PushMessageContentContact(PushMessageContent):
    """
    A message with a user contact

    :param name: Contact's name
    :param is_pinned: True, if the message is a pinned message with the specified content
    """
    __slots__ = ("name", "is_pinned", "_extra", "_client_id", "_type")

    def __init__(self, name = None, is_pinned = None):
        self.name = name
        self.is_pinned = is_pinned
        self._type = "pushMessageContentContact"