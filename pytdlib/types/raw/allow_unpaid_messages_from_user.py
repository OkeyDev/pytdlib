from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class AllowUnpaidMessagesFromUser(Function):
    """
    Allows the specified user to send unpaid private messages to the current user by adding a rule to userPrivacySettingAllowUnpaidMessages

    :param user_id: Identifier of the user
    :param refund_payments: Pass true to refund the user previously paid messages
    :return: :class:`Ok`
    """
    __slots__ = ("user_id", "refund_payments", "_extra", "_client_id", "_type")

    def __init__(self, user_id = None, refund_payments = None):
        self.user_id = user_id
        self.refund_payments = refund_payments
        self._type = "allowUnpaidMessagesFromUser"