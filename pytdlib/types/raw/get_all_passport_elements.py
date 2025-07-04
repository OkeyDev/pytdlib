from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class GetAllPassportElements(Function):
    """
    Returns all available Telegram Passport elements

    :param password: The 2-step verification password of the current user
    :return: :class:`PassportElements`
    """
    __slots__ = ("password", "_extra", "_client_id", "_type")

    def __init__(self, password = None):
        self.password = password
        self._type = "getAllPassportElements"