from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class GetChatFolderNewChats(Function):
    """
    Returns new chats added to a shareable chat folder by its owner. The method must be called at most once in getOption("chat_folder_new_chats_update_period") for the given chat folder

    :param chat_folder_id: Chat folder identifier
    :return: :class:`Chats`
    """
    __slots__ = ("chat_folder_id", "_extra", "_client_id", "_type")

    def __init__(self, chat_folder_id = None):
        self.chat_folder_id = chat_folder_id
        self._type = "getChatFolderNewChats"