from .reset_password_result import ResetPasswordResult

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class ResetPasswordResultPending(ResetPasswordResult):
    """
    The password reset request is pending

    :param pending_reset_date: Point in time (Unix timestamp) after which the password can be reset immediately using resetPassword
    """
    __slots__ = ("pending_reset_date", "_extra", "_client_id", "_type")

    def __init__(self, pending_reset_date = None):
        self.pending_reset_date = pending_reset_date
        self._type = "resetPasswordResultPending"