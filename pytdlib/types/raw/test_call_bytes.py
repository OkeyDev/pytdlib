from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class TestCallBytes(Function):
    """
    Returns the received bytes; for testing only. This is an offline method. Can be called before authorization

    :param x: Bytes to return
    :return: :class:`TestBytes`
    """
    __slots__ = ("x", "_extra", "_client_id", "_type")

    def __init__(self, x = None):
        self.x = x
        self._type = "testCallBytes"