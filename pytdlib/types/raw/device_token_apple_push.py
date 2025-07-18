from .device_token import DeviceToken

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class DeviceTokenApplePush(DeviceToken):
    """
    A token for Apple Push Notification service

    :param device_token: Device token; may be empty to deregister a device
    :param is_app_sandbox: True, if App Sandbox is enabled
    """
    __slots__ = ("device_token", "is_app_sandbox", "_extra", "_client_id", "_type")

    def __init__(self, device_token = None, is_app_sandbox = None):
        self.device_token = device_token
        self.is_app_sandbox = is_app_sandbox
        self._type = "deviceTokenApplePush"