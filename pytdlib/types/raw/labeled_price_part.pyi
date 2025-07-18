from .object_base import ObjectBase

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class LabeledPricePart(ObjectBase):
    """
    Portion of the price of a product (e.g., "delivery cost", "tax amount")

    :param label: Label for this portion of the product price
    :param amount: Currency amount in the smallest units of the currency
    """
    __slots__ = ("label", "amount", "_extra", "_client_id", "_type")

    def __init__(self, label: str = "", amount: int = 0):
        self.label = label
        self.amount = amount
        self._type = "labeledPricePart"