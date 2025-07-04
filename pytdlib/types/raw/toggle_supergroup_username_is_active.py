from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class ToggleSupergroupUsernameIsActive(Function):
    """
    Changes active state for a username of a supergroup or channel, requires owner privileges in the supergroup or channel. The editable username can't be disabled. May return an error with a message "USERNAMES_ACTIVE_TOO_MUCH" if the maximum number of active usernames has been reached

    :param supergroup_id: Identifier of the supergroup or channel
    :param username: The username to change
    :param is_active: Pass true to activate the username; pass false to disable it
    :return: :class:`Ok`
    """
    __slots__ = ("supergroup_id", "username", "is_active", "_extra", "_client_id", "_type")

    def __init__(self, supergroup_id = None, username = None, is_active = None):
        self.supergroup_id = supergroup_id
        self.username = username
        self.is_active = is_active
        self._type = "toggleSupergroupUsernameIsActive"