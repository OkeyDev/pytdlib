from .object_base import ObjectBase

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class BotInfo(ObjectBase):
    """
    Contains information about a bot

    :param short_description: The text that is shown on the bot's profile page and is sent together with the link when users share the bot
    :param description: Contains information about a bot
    :param photo: Photo shown in the chat with the bot if the chat is empty; may be null
    :param animation: Animation shown in the chat with the bot if the chat is empty; may be null
    :param menu_button: Information about a button to show instead of the bot commands menu button; may be null if ordinary bot commands menu must be shown
    :param commands: List of the bot commands
    :param privacy_policy_url: The HTTP link to the privacy policy of the bot. If empty, then /privacy command must be used if supported by the bot. If the command isn't supported, then https://telegram.org/privacy-tpa must be opened
    :param default_group_administrator_rights: Default administrator rights for adding the bot to basic group and supergroup chats; may be null
    :param default_channel_administrator_rights: Default administrator rights for adding the bot to channels; may be null
    :param affiliate_program: Information about the affiliate program of the bot; may be null if none
    :param web_app_background_light_color: Default light background color for bot Web Apps; -1 if not specified
    :param web_app_background_dark_color: Default dark background color for bot Web Apps; -1 if not specified
    :param web_app_header_light_color: Default light header color for bot Web Apps; -1 if not specified
    :param web_app_header_dark_color: Default dark header color for bot Web Apps; -1 if not specified
    :param verification_parameters: Parameters of the verification that can be provided by the bot; may be null if none or the current user isn't the owner of the bot
    :param can_get_revenue_statistics: True, if the bot's revenue statistics are available to the current user
    :param can_manage_emoji_status: True, if the bot can manage emoji status of the current user
    :param has_media_previews: True, if the bot has media previews
    :param edit_commands_link: The internal link, which can be used to edit bot commands; may be null
    :param edit_description_link: The internal link, which can be used to edit bot description; may be null
    :param edit_description_media_link: The internal link, which can be used to edit the photo or animation shown in the chat with the bot if the chat is empty; may be null
    :param edit_settings_link: The internal link, which can be used to edit bot settings; may be null
    """
    __slots__ = ("short_description", "description", "photo", "animation", "menu_button", "commands", "privacy_policy_url", "default_group_administrator_rights", "default_channel_administrator_rights", "affiliate_program", "web_app_background_light_color", "web_app_background_dark_color", "web_app_header_light_color", "web_app_header_dark_color", "verification_parameters", "can_get_revenue_statistics", "can_manage_emoji_status", "has_media_previews", "edit_commands_link", "edit_description_link", "edit_description_media_link", "edit_settings_link", "_extra", "_client_id", "_type")

    def __init__(self, short_description = None, description = None, photo = None, animation = None, menu_button = None, commands = None, privacy_policy_url = None, default_group_administrator_rights = None, default_channel_administrator_rights = None, affiliate_program = None, web_app_background_light_color = None, web_app_background_dark_color = None, web_app_header_light_color = None, web_app_header_dark_color = None, verification_parameters = None, can_get_revenue_statistics = None, can_manage_emoji_status = None, has_media_previews = None, edit_commands_link = None, edit_description_link = None, edit_description_media_link = None, edit_settings_link = None):
        self.short_description = short_description
        self.description = description
        self.photo = photo
        self.animation = animation
        self.menu_button = menu_button
        self.commands = commands
        self.privacy_policy_url = privacy_policy_url
        self.default_group_administrator_rights = default_group_administrator_rights
        self.default_channel_administrator_rights = default_channel_administrator_rights
        self.affiliate_program = affiliate_program
        self.web_app_background_light_color = web_app_background_light_color
        self.web_app_background_dark_color = web_app_background_dark_color
        self.web_app_header_light_color = web_app_header_light_color
        self.web_app_header_dark_color = web_app_header_dark_color
        self.verification_parameters = verification_parameters
        self.can_get_revenue_statistics = can_get_revenue_statistics
        self.can_manage_emoji_status = can_manage_emoji_status
        self.has_media_previews = has_media_previews
        self.edit_commands_link = edit_commands_link
        self.edit_description_link = edit_description_link
        self.edit_description_media_link = edit_description_media_link
        self.edit_settings_link = edit_settings_link
        self._type = "botInfo"