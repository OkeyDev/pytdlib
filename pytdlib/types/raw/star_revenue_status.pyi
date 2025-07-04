from .object_base import ObjectBase
from .star_amount import StarAmount

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class StarRevenueStatus(ObjectBase):
    """
    Contains information about Telegram Stars earned by a bot or a chat

    :param total_amount: Total amount of Telegram Stars earned
    :param current_amount: The amount of Telegram Stars that aren't withdrawn yet
    :param available_amount: The amount of Telegram Stars that are available for withdrawal
    :param withdrawal_enabled: True, if Telegram Stars can be withdrawn now or later
    :param next_withdrawal_in: Time left before the next withdrawal can be started, in seconds; 0 if withdrawal can be started now
    """
    __slots__ = ("total_amount", "current_amount", "available_amount", "withdrawal_enabled", "next_withdrawal_in", "_extra", "_client_id", "_type")

    def __init__(self, total_amount: StarAmount | None = None, current_amount: StarAmount | None = None, available_amount: StarAmount | None = None, withdrawal_enabled: bool = False, next_withdrawal_in: int = 0):
        self.total_amount = total_amount
        self.current_amount = current_amount
        self.available_amount = available_amount
        self.withdrawal_enabled = withdrawal_enabled
        self.next_withdrawal_in = next_withdrawal_in
        self._type = "starRevenueStatus"