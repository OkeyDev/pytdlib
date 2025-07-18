from .function import Function

from .message import Message

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class SetGameScore(Function[Message]):
    """
    Updates the game score of the specified user in the game; for bots only

    :param chat_id: The chat to which the message with the game belongs
    :param message_id: Identifier of the message
    :param edit_message: Pass true to edit the game message to include the current scoreboard
    :param user_id: User identifier
    :param score: The new score
    :param force: Pass true to update the score even if it decreases. If the score is 0, the user will be deleted from the high score table
    :return: :class:`Message`
    """
    __slots__ = ("chat_id", "message_id", "edit_message", "user_id", "score", "force", "_extra", "_client_id", "_type")

    def __init__(self, chat_id: int = 0, message_id: int = 0, edit_message: bool = False, user_id: int = 0, score: int = 0, force: bool = False):
        self.chat_id = chat_id
        self.message_id = message_id
        self.edit_message = edit_message
        self.user_id = user_id
        self.score = score
        self.force = force
        self._type = "setGameScore"