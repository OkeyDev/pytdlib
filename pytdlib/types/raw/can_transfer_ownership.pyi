from .function import Function

from .can_transfer_ownership_result_ok import CanTransferOwnershipResultOk
from .can_transfer_ownership_result_password_needed import CanTransferOwnershipResultPasswordNeeded
from .can_transfer_ownership_result_password_too_fresh import CanTransferOwnershipResultPasswordTooFresh
from .can_transfer_ownership_result_session_too_fresh import CanTransferOwnershipResultSessionTooFresh

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class CanTransferOwnership(Function[CanTransferOwnershipResultOk | CanTransferOwnershipResultPasswordNeeded | CanTransferOwnershipResultPasswordTooFresh | CanTransferOwnershipResultSessionTooFresh]):
    """
    Checks whether the current session can be used to transfer a chat ownership to another user

    :return: :class:`CanTransferOwnershipResultOk | CanTransferOwnershipResultPasswordNeeded | CanTransferOwnershipResultPasswordTooFresh | CanTransferOwnershipResultSessionTooFresh`
    """
    __slots__ = ("_extra", "_client_id", "_type")

    def __init__(self):

        self._type = "canTransferOwnership"