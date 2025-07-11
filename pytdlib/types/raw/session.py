from .object_base import ObjectBase

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class Session(ObjectBase):
    """
    Contains information about one session in a Telegram application used by the current user. Sessions must be shown to the user in the returned order

    :param id: Session identifier
    :param is_current: True, if this session is the current session
    :param is_password_pending: True, if a 2-step verification password is needed to complete authorization of the session
    :param is_unconfirmed: True, if the session wasn't confirmed from another session
    :param can_accept_secret_chats: True, if incoming secret chats can be accepted by the session
    :param can_accept_calls: True, if incoming calls can be accepted by the session
    :param type: Session type based on the system and application version, which can be used to display a corresponding icon
    :param api_id: Telegram API identifier, as provided by the application
    :param application_name: Name of the application, as provided by the application
    :param application_version: The version of the application, as provided by the application
    :param is_official_application: True, if the application is an official application or uses the api_id of an official application
    :param device_model: Model of the device the application has been run or is running on, as provided by the application
    :param platform: Operating system the application has been run or is running on, as provided by the application
    :param system_version: Version of the operating system the application has been run or is running on, as provided by the application
    :param log_in_date: Point in time (Unix timestamp) when the user has logged in
    :param last_active_date: Point in time (Unix timestamp) when the session was last used
    :param ip_address: IP address from which the session was created, in human-readable format
    :param location: A human-readable description of the location from which the session was created, based on the IP address
    """
    __slots__ = ("id", "is_current", "is_password_pending", "is_unconfirmed", "can_accept_secret_chats", "can_accept_calls", "type", "api_id", "application_name", "application_version", "is_official_application", "device_model", "platform", "system_version", "log_in_date", "last_active_date", "ip_address", "location", "_extra", "_client_id", "_type")

    def __init__(self, id = None, is_current = None, is_password_pending = None, is_unconfirmed = None, can_accept_secret_chats = None, can_accept_calls = None, type = None, api_id = None, application_name = None, application_version = None, is_official_application = None, device_model = None, platform = None, system_version = None, log_in_date = None, last_active_date = None, ip_address = None, location = None):
        self.id = id
        self.is_current = is_current
        self.is_password_pending = is_password_pending
        self.is_unconfirmed = is_unconfirmed
        self.can_accept_secret_chats = can_accept_secret_chats
        self.can_accept_calls = can_accept_calls
        self.type = type
        self.api_id = api_id
        self.application_name = application_name
        self.application_version = application_version
        self.is_official_application = is_official_application
        self.device_model = device_model
        self.platform = platform
        self.system_version = system_version
        self.log_in_date = log_in_date
        self.last_active_date = last_active_date
        self.ip_address = ip_address
        self.location = location
        self._type = "session"