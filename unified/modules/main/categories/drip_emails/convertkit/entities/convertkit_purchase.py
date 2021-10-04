from dataclasses import dataclass
from unified.core import util

@dataclass
class ConvertkitPurchase:
    purchase_id: str = None
    transaction_id: str = None
    email: str = None
    subtotal: str = None
    tax: str = None
    shipping: str = None
    discount: str = None
    total: str = None
    currency_id: str = None
    transaction_time: str = None
    status: str = None
    product_name: str = None
    product_id: str = None
    product_sku: str = None
    product_price: str = None
    product_quantity: str = None
    list_id: str = None

    def __post_init__(self):
        if not(self.transaction_time is None or "-" in self.transaction_time):
            format = '%Y-%m-%d'
            self.transaction_time = util.epoch_to_format(format, self.transaction_time)
