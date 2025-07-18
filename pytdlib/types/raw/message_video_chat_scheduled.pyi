from .message_content import MessageContent

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class MessageVideoChatScheduled(MessageContent):
    """
    A new video chat was scheduled

    :param group_call_id: Identifier of the video chat. The video chat can be received through the method getGroupCall
    :param start_date: Point in time (Unix timestamp) when the group call is expected to be started by an administrator
    """
    __slots__ = ("group_call_id", "start_date", "_extra", "_client_id", "_type")

    def __init__(self, group_call_id: int = 0, start_date: int = 0):
        self.group_call_id = group_call_id
        self.start_date = start_date
        self._type = "messageVideoChatScheduled"