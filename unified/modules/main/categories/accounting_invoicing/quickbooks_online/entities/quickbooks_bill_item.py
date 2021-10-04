from dataclasses import dataclass
from accounting_invoicing.quickbooks_online import util

@dataclass
class QuickbooksonlineBillItem:
    vendor_id: str = None
    bill_number: str = None
    line_item_id: str = None
    line_description: str = None
    quantity: str = None
    unit_price: str = None
    ap_account_id: str = None
    customer_id: str = None
    due_date: str = None
    transaction_date: str = None

    def __post_init__(self):
        if not(self.due_date is None or "-" in self.due_date):
            format = '%Y-%m-%d'
            self.due_date = util.epoch_to_format(
                format, self.due_date)
        if not(self.transaction_date is None or "-" in self.transaction_date):
            format = '%Y-%m-%d'
            self.transaction_date = util.epoch_to_format(
                format, self.transaction_date)
