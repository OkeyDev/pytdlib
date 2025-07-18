from .message_content import MessageContent

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class MessageForumTopicIsHiddenToggled(MessageContent):
    """
    A General forum topic has been hidden or unhidden

    :param is_hidden: True, if the topic was hidden; otherwise, the topic was unhidden
    """
    __slots__ = ("is_hidden", "_extra", "_client_id", "_type")

    def __init__(self, is_hidden = None):
        self.is_hidden = is_hidden
        self._type = "messageForumTopicIsHiddenToggled"