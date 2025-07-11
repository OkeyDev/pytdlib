from .object_base import ObjectBase

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class BotMediaPreview(ObjectBase):
    """
    Describes media previews of a bot

    :param date: Point in time (Unix timestamp) when the preview was added or changed last time
    :param content: Content of the preview
    """
    __slots__ = ("date", "content", "_extra", "_client_id", "_type")

    def __init__(self, date = None, content = None):
        self.date = date
        self.content = content
        self._type = "botMediaPreview"