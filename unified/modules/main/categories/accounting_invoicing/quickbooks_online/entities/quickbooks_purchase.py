from dataclasses import dataclass
from accounting_invoicing.quickbooks_online import util


@dataclass
class QuickbooksonlinePurchase:
    purchase_id: str = None
    vendor_id: str = None
    purchase_order_date: str = None
    purchase_order_number: str = None
    account_type_id: str = None
    account_description: str = None
    account_amount: str = None
    account_customer_id: str = None
    product_id: str = None
    product_description: str = None
    product_quantity: str = None
    product_rate: str = None
    product_amount: str = None
    product_customer_id: str = None
    your_message_to_vendor: str = None
    memo: str = None

    def __post_init__(self):
        if not(self.purchase_order_date is None or "-" in self.purchase_order_date):
            format = '%Y-%m-%d'
            self.purchase_order_date = util.epoch_to_format(
                format, self.purchase_order_date)
