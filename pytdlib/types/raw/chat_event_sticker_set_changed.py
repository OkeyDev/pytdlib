from .chat_event_action import ChatEventAction

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class ChatEventStickerSetChanged(ChatEventAction):
    """
    The supergroup sticker set was changed

    :param old_sticker_set_id: Previous identifier of the chat sticker set; 0 if none
    :param new_sticker_set_id: New identifier of the chat sticker set; 0 if none
    """
    __slots__ = ("old_sticker_set_id", "new_sticker_set_id", "_extra", "_client_id", "_type")

    def __init__(self, old_sticker_set_id = None, new_sticker_set_id = None):
        self.old_sticker_set_id = old_sticker_set_id
        self.new_sticker_set_id = new_sticker_set_id
        self._type = "chatEventStickerSetChanged"