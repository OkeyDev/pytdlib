from .user_type import UserType

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class UserTypeUnknown(UserType):
    """
    No information on the user besides the user identifier is available, yet this user has not been deleted. This object is extremely rare and must be handled like a deleted user. It is not possible to perform any actions on users of this type

    """
    __slots__ = ("_extra", "_client_id", "_type")

    def __init__(self):

        self._type = "userTypeUnknown"