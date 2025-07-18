from .message_content import MessageContent

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class MessageChatUpgradeTo(MessageContent):
    """
    A basic group was upgraded to a supergroup and was deactivated as the result

    :param supergroup_id: Identifier of the supergroup to which the basic group was upgraded
    """
    __slots__ = ("supergroup_id", "_extra", "_client_id", "_type")

    def __init__(self, supergroup_id = None):
        self.supergroup_id = supergroup_id
        self._type = "messageChatUpgradeTo"