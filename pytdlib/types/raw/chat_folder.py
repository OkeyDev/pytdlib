from .object_base import ObjectBase

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class ChatFolder(ObjectBase):
    """
    Represents a folder for user chats

    :param name: The name of the folder
    :param icon: The chosen icon for the chat folder; may be null. If null, use getChatFolderDefaultIconName to get default icon name for the folder
    :param color_id: The identifier of the chosen color for the chat folder icon; from -1 to 6. If -1, then color is disabled. Can't be changed if folder tags are disabled or the current user doesn't have Telegram Premium subscription
    :param is_shareable: True, if at least one link has been created for the folder
    :param pinned_chat_ids: The chat identifiers of pinned chats in the folder. There can be up to getOption("chat_folder_chosen_chat_count_max") pinned and always included non-secret chats and the same number of secret chats, but the limit can be increased with Telegram Premium
    :param included_chat_ids: The chat identifiers of always included chats in the folder. There can be up to getOption("chat_folder_chosen_chat_count_max") pinned and always included non-secret chats and the same number of secret chats, but the limit can be increased with Telegram Premium
    :param excluded_chat_ids: The chat identifiers of always excluded chats in the folder. There can be up to getOption("chat_folder_chosen_chat_count_max") always excluded non-secret chats and the same number of secret chats, but the limit can be increased with Telegram Premium
    :param exclude_muted: True, if muted chats need to be excluded
    :param exclude_read: True, if read chats need to be excluded
    :param exclude_archived: True, if archived chats need to be excluded
    :param include_contacts: True, if contacts need to be included
    :param include_non_contacts: True, if non-contact users need to be included
    :param include_bots: True, if bots need to be included
    :param include_groups: True, if basic groups and supergroups need to be included
    :param include_channels: True, if channels need to be included
    """
    __slots__ = ("name", "icon", "color_id", "is_shareable", "pinned_chat_ids", "included_chat_ids", "excluded_chat_ids", "exclude_muted", "exclude_read", "exclude_archived", "include_contacts", "include_non_contacts", "include_bots", "include_groups", "include_channels", "_extra", "_client_id", "_type")

    def __init__(self, name = None, icon = None, color_id = None, is_shareable = None, pinned_chat_ids = None, included_chat_ids = None, excluded_chat_ids = None, exclude_muted = None, exclude_read = None, exclude_archived = None, include_contacts = None, include_non_contacts = None, include_bots = None, include_groups = None, include_channels = None):
        self.name = name
        self.icon = icon
        self.color_id = color_id
        self.is_shareable = is_shareable
        self.pinned_chat_ids = pinned_chat_ids
        self.included_chat_ids = included_chat_ids
        self.excluded_chat_ids = excluded_chat_ids
        self.exclude_muted = exclude_muted
        self.exclude_read = exclude_read
        self.exclude_archived = exclude_archived
        self.include_contacts = include_contacts
        self.include_non_contacts = include_non_contacts
        self.include_bots = include_bots
        self.include_groups = include_groups
        self.include_channels = include_channels
        self._type = "chatFolder"