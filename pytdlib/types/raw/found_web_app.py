from .object_base import ObjectBase

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class FoundWebApp(ObjectBase):
    """
    Contains information about a Web App found by its short name

    :param web_app: The Web App
    :param request_write_access: True, if the user must be asked for the permission to the bot to send them messages
    :param skip_confirmation: True, if there is no need to show an ordinary open URL confirmation before opening the Web App. The field must be ignored and confirmation must be shown anyway if the Web App link was hidden
    """
    __slots__ = ("web_app", "request_write_access", "skip_confirmation", "_extra", "_client_id", "_type")

    def __init__(self, web_app = None, request_write_access = None, skip_confirmation = None):
        self.web_app = web_app
        self.request_write_access = request_write_access
        self.skip_confirmation = skip_confirmation
        self._type = "foundWebApp"