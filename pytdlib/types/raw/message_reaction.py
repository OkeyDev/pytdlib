from .object_base import ObjectBase

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class MessageReaction(ObjectBase):
    """
    Contains information about a reaction to a message

    :param type: Type of the reaction
    :param total_count: Number of times the reaction was added
    :param is_chosen: True, if the reaction is chosen by the current user
    :param used_sender_id: Identifier of the message sender used by the current user to add the reaction; may be null if unknown or the reaction isn't chosen
    :param recent_sender_ids: Identifiers of at most 3 recent message senders, added the reaction; available in private, basic group and supergroup chats
    """
    __slots__ = ("type", "total_count", "is_chosen", "used_sender_id", "recent_sender_ids", "_extra", "_client_id", "_type")

    def __init__(self, type = None, total_count = None, is_chosen = None, used_sender_id = None, recent_sender_ids = None):
        self.type = type
        self.total_count = total_count
        self.is_chosen = is_chosen
        self.used_sender_id = used_sender_id
        self.recent_sender_ids = recent_sender_ids
        self._type = "messageReaction"