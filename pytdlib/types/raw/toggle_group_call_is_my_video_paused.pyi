from .function import Function

from .ok import Ok

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class ToggleGroupCallIsMyVideoPaused(Function[Ok]):
    """
    Toggles whether current user's video is paused

    :param group_call_id: Group call identifier
    :param is_my_video_paused: Pass true if the current user's video is paused
    :return: :class:`Ok`
    """
    __slots__ = ("group_call_id", "is_my_video_paused", "_extra", "_client_id", "_type")

    def __init__(self, group_call_id: int = 0, is_my_video_paused: bool = False):
        self.group_call_id = group_call_id
        self.is_my_video_paused = is_my_video_paused
        self._type = "toggleGroupCallIsMyVideoPaused"