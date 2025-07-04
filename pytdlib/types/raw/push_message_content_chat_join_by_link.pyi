from .push_message_content import PushMessageContent

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class PushMessageContentChatJoinByLink(PushMessageContent):
    """
    A new member joined the chat via an invite link

    """
    __slots__ = ("_extra", "_client_id", "_type")

    def __init__(self):

        self._type = "pushMessageContentChatJoinByLink"