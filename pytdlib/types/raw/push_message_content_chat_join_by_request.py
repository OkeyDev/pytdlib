from .push_message_content import PushMessageContent

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class PushMessageContentChatJoinByRequest(PushMessageContent):
    """
    A new member was accepted to the chat by an administrator

    """
    __slots__ = ("_extra", "_client_id", "_type")

    def __init__(self):

        self._type = "pushMessageContentChatJoinByRequest"