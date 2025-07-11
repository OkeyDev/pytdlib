from .object_base import ObjectBase

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class MessageLinkInfo(ObjectBase):
    """
    Contains information about a link to a message or a forum topic in a chat

    :param is_public: True, if the link is a public link for a message or a forum topic in a chat
    :param chat_id: If found, identifier of the chat to which the link points, 0 otherwise
    :param message_thread_id: If found, identifier of the message thread in which to open the message, or a forum topic to open if the message is missing
    :param message: If found, the linked message; may be null
    :param media_timestamp: Timestamp from which the video/audio/video note/voice note/story playing must start, in seconds; 0 if not specified. The media can be in the message content or in its link preview
    :param for_album: True, if the whole media album to which the message belongs is linked
    """
    __slots__ = ("is_public", "chat_id", "message_thread_id", "message", "media_timestamp", "for_album", "_extra", "_client_id", "_type")

    def __init__(self, is_public = None, chat_id = None, message_thread_id = None, message = None, media_timestamp = None, for_album = None):
        self.is_public = is_public
        self.chat_id = chat_id
        self.message_thread_id = message_thread_id
        self.message = message
        self.media_timestamp = media_timestamp
        self.for_album = for_album
        self._type = "messageLinkInfo"