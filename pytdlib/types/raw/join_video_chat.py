from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class JoinVideoChat(Function):
    """
    Joins an active video chat. Returns join response payload for tgcalls

    :param group_call_id: Group call identifier
    :param participant_id: Identifier of a group call participant, which will be used to join the call; pass null to join as self; video chats only
    :param join_parameters: Parameters to join the call
    :param invite_hash: Invite hash as received from internalLinkTypeVideoChat
    :return: :class:`Text`
    """
    __slots__ = ("group_call_id", "participant_id", "join_parameters", "invite_hash", "_extra", "_client_id", "_type")

    def __init__(self, group_call_id = None, participant_id = None, join_parameters = None, invite_hash = None):
        self.group_call_id = group_call_id
        self.participant_id = participant_id
        self.join_parameters = join_parameters
        self.invite_hash = invite_hash
        self._type = "joinVideoChat"