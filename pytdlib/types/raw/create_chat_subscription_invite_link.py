from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class CreateChatSubscriptionInviteLink(Function):
    """
    Creates a new subscription invite link for a channel chat. Requires can_invite_users right in the chat

    :param chat_id: Chat identifier
    :param name: Invite link name; 0-32 characters
    :param subscription_pricing: Information about subscription plan that will be applied to the users joining the chat via the link. Subscription period must be 2592000 in production environment, and 60 or 300 if Telegram test environment is used
    :return: :class:`ChatInviteLink`
    """
    __slots__ = ("chat_id", "name", "subscription_pricing", "_extra", "_client_id", "_type")

    def __init__(self, chat_id = None, name = None, subscription_pricing = None):
        self.chat_id = chat_id
        self.name = name
        self.subscription_pricing = subscription_pricing
        self._type = "createChatSubscriptionInviteLink"