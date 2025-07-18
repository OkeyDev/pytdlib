from .update import Update

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class UpdateStoryStealthMode(Update):
    """
    Story stealth mode settings have changed

    :param active_until_date: Point in time (Unix timestamp) until stealth mode is active; 0 if it is disabled
    :param cooldown_until_date: Point in time (Unix timestamp) when stealth mode can be enabled again; 0 if there is no active cooldown
    """
    __slots__ = ("active_until_date", "cooldown_until_date", "_extra", "_client_id", "_type")

    def __init__(self, active_until_date: int = 0, cooldown_until_date: int = 0):
        self.active_until_date = active_until_date
        self.cooldown_until_date = cooldown_until_date
        self._type = "updateStoryStealthMode"