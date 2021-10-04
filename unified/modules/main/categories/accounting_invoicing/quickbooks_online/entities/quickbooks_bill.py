from dataclasses import dataclass
from accounting_invoicing.quickbooks_online import util


@dataclass
class QuickbooksonlineBill:
    bill_id:str=None
    vendor_id: str = None
    terms: str = None
    transaction_date: str = None
    due_date: str = None
    bill_number: str = None
    currency: str = None
    global_tax_calculation: str = None
    line_item_description: str = None
    line_item_amount: str = None
    line_tax: str = None
    line_item_billable: str = None
    line_item_customer_id: str = None
    account_type_id: str = None
    line_item_tax_code: str = None,
    ap_account_id: str = None
    memo: str = None
    line_quantity: str = None
    line_id: str = None
    line_rate: str = None

    def __post_init__(self):
        if not(self.due_date is None or "-" in self.due_date):
            format = '%Y-%m-%d'
            self.due_date = util.epoch_to_format(
                format, self.due_date)
        if not(self.transaction_date is None or "-" in self.transaction_date):
            format = '%Y-%m-%d'
            self.transaction_date = util.epoch_to_format(
                format, self.transaction_date)