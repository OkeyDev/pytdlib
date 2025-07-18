from .chat_background import ChatBackground
from .message_content import MessageContent

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class MessageChatSetBackground(MessageContent):
    """
    A new background was set in the chat

    :param old_background_message_id: Identifier of the message with a previously set same background; 0 if none. Can be an identifier of a deleted message
    :param background: The new background
    :param only_for_self: True, if the background was set only for self
    """
    __slots__ = ("old_background_message_id", "background", "only_for_self", "_extra", "_client_id", "_type")

    def __init__(self, old_background_message_id: int = 0, background: ChatBackground | None = None, only_for_self: bool = False):
        self.old_background_message_id = old_background_message_id
        self.background = background
        self.only_for_self = only_for_self
        self._type = "messageChatSetBackground"