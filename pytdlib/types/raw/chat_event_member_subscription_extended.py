from .chat_event_action import ChatEventAction

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class ChatEventMemberSubscriptionExtended(ChatEventAction):
    """
    A chat member extended their subscription to the chat

    :param user_id: Affected chat member user identifier
    :param old_status: Previous status of the chat member
    :param new_status: New status of the chat member
    """
    __slots__ = ("user_id", "old_status", "new_status", "_extra", "_client_id", "_type")

    def __init__(self, user_id = None, old_status = None, new_status = None):
        self.user_id = user_id
        self.old_status = old_status
        self.new_status = new_status
        self._type = "chatEventMemberSubscriptionExtended"