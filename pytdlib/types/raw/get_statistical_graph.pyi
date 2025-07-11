from .function import Function

from .statistical_graph_async import StatisticalGraphAsync
from .statistical_graph_data import StatisticalGraphData
from .statistical_graph_error import StatisticalGraphError

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class GetStatisticalGraph(Function[StatisticalGraphData | StatisticalGraphAsync | StatisticalGraphError]):
    """
    Loads an asynchronous or a zoomed in statistical graph

    :param chat_id: Chat identifier
    :param token: The token for graph loading
    :param x: X-value for zoomed in graph or 0 otherwise
    :return: :class:`StatisticalGraphData | StatisticalGraphAsync | StatisticalGraphError`
    """
    __slots__ = ("chat_id", "token", "x", "_extra", "_client_id", "_type")

    def __init__(self, chat_id: int = 0, token: str = "", x: int = 0):
        self.chat_id = chat_id
        self.token = token
        self.x = x
        self._type = "getStatisticalGraph"