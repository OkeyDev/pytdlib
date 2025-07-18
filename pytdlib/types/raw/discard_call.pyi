from .function import Function

from .ok import Ok

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class DiscardCall(Function[Ok]):
    """
    Discards a call

    :param call_id: Call identifier
    :param is_disconnected: Pass true if the user was disconnected
    :param invite_link: If the call was upgraded to a group call, pass invite link to the group call
    :param duration: The call duration, in seconds
    :param is_video: Pass true if the call was a video call
    :param connection_id: Identifier of the connection used during the call
    :return: :class:`Ok`
    """
    __slots__ = ("call_id", "is_disconnected", "invite_link", "duration", "is_video", "connection_id", "_extra", "_client_id", "_type")

    def __init__(self, call_id: int = 0, is_disconnected: bool = False, invite_link: str = "", duration: int = 0, is_video: bool = False, connection_id: int = 0):
        self.call_id = call_id
        self.is_disconnected = is_disconnected
        self.invite_link = invite_link
        self.duration = duration
        self.is_video = is_video
        self.connection_id = connection_id
        self._type = "discardCall"