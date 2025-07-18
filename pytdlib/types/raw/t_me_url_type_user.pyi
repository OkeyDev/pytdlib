from .t_me_url_type import TMeUrlType

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class TMeUrlTypeUser(TMeUrlType):
    """
    A URL linking to a user

    :param user_id: Identifier of the user
    """
    __slots__ = ("user_id", "_extra", "_client_id", "_type")

    def __init__(self, user_id: int = 0):
        self.user_id = user_id
        self._type = "tMeUrlTypeUser"