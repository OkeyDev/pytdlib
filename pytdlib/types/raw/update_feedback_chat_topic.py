from .update import Update

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class UpdateFeedbackChatTopic(Update):
    """
    Basic information about a topic in a feedback group has changed. This update is guaranteed to come before the topic identifier is returned to the application

    :param topic: New data about the topic
    """
    __slots__ = ("topic", "_extra", "_client_id", "_type")

    def __init__(self, topic = None):
        self.topic = topic
        self._type = "updateFeedbackChatTopic"