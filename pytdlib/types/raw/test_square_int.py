from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class TestSquareInt(Function):
    """
    Returns the squared received number; for testing only. This is an offline method. Can be called before authorization

    :param x: Number to square
    :return: :class:`TestInt`
    """
    __slots__ = ("x", "_extra", "_client_id", "_type")

    def __init__(self, x = None):
        self.x = x
        self._type = "testSquareInt"