from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class SendInlineQueryResultMessage(Function):
    """
    Sends the result of an inline query as a message. Returns the sent message. Always clears a chat draft message

    :param chat_id: Target chat
    :param message_thread_id: If not 0, the message thread identifier in which the message will be sent
    :param reply_to: Information about the message or story to be replied; pass null if none
    :param options: Options to be used to send the message; pass null to use default options
    :param query_id: Identifier of the inline query
    :param result_id: Identifier of the inline query result
    :param hide_via_bot: Pass true to hide the bot, via which the message is sent. Can be used only for bots getOption("animation_search_bot_username"), getOption("photo_search_bot_username"), and getOption("venue_search_bot_username")
    :return: :class:`Message`
    """
    __slots__ = ("chat_id", "message_thread_id", "reply_to", "options", "query_id", "result_id", "hide_via_bot", "_extra", "_client_id", "_type")

    def __init__(self, chat_id = None, message_thread_id = None, reply_to = None, options = None, query_id = None, result_id = None, hide_via_bot = None):
        self.chat_id = chat_id
        self.message_thread_id = message_thread_id
        self.reply_to = reply_to
        self.options = options
        self.query_id = query_id
        self.result_id = result_id
        self.hide_via_bot = hide_via_bot
        self._type = "sendInlineQueryResultMessage"