from .update import Update

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class UpdateForumTopicInfo(Update):
    """
    Basic information about a topic in a forum chat was changed

    :param info: New information about the topic
    """
    __slots__ = ("info", "_extra", "_client_id", "_type")

    def __init__(self, info = None):
        self.info = info
        self._type = "updateForumTopicInfo"