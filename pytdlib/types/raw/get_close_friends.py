from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class GetCloseFriends(Function):
    """
    Returns all close friends of the current user

    :return: :class:`Users`
    """
    __slots__ = ("_extra", "_client_id", "_type")

    def __init__(self):

        self._type = "getCloseFriends"