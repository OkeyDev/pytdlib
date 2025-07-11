from .chat_event_action import ChatEventAction

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class ChatEventShowMessageSenderToggled(ChatEventAction):
    """
    The show_message_sender setting of a channel was toggled

    :param show_message_sender: New value of show_message_sender
    """
    __slots__ = ("show_message_sender", "_extra", "_client_id", "_type")

    def __init__(self, show_message_sender: bool = False):
        self.show_message_sender = show_message_sender
        self._type = "chatEventShowMessageSenderToggled"