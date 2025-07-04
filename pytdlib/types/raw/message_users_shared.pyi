from .message_content import MessageContent
from .shared_user import SharedUser
from typing import List

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class MessageUsersShared(MessageContent):
    """
    The current user shared users, which were requested by the bot

    :param users: The shared users
    :param button_id: Identifier of the keyboard button with the request
    """
    __slots__ = ("users", "button_id", "_extra", "_client_id", "_type")

    def __init__(self, users: List[SharedUser] | None = None, button_id: int = 0):
        self.users = users
        self.button_id = button_id
        self._type = "messageUsersShared"