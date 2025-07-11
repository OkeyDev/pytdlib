from .object_base import ObjectBase

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class ChatJoinRequest(ObjectBase):
    """
    Describes a user that sent a join request and waits for administrator approval

    :param user_id: User identifier
    :param date: Point in time (Unix timestamp) when the user sent the join request
    :param bio: A short bio of the user
    """
    __slots__ = ("user_id", "date", "bio", "_extra", "_client_id", "_type")

    def __init__(self, user_id = None, date = None, bio = None):
        self.user_id = user_id
        self.date = date
        self.bio = bio
        self._type = "chatJoinRequest"