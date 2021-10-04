from dataclasses import dataclass
from accounting_invoicing.quickbooks_online import util

@dataclass
class QuickbooksonlineCreditMemo:
    customer_id: str = None
    send_later: str = None
    terms: str = None
    due_date: str = None
    invoice_number: str = None
    product_id: str = None
    product_description: str = None
    message_displayed_on_credit_memo: str = None
    message_displayed_on_statement: str = None
    product_quantity: int = 0
    product_amount: str = None
    product_tax: str = None
    product_rate: int = 0
    # invoice_date: str = None
    invoice_id: str = None
    email: str = None
    vendor_id: str = None
    transaction_date: str = None
    bill_number: str = None
    product_billable: str = None
    memo: str = None
    credit_memo_date: str = None
    credit_memo_number: str = None
    product_service_date:str=None
    apply_tax_after_discount:str=None

    def __post_init__(self):
        if not(self.product_service_date is None or "-" in self.product_service_date):
            format = '%Y-%m-%d'
            self.product_service_date = util.epoch_to_format(
                format, self.product_service_date)
        if not(self.credit_memo_date is None or "-" in self.credit_memo_date):
            format = '%Y-%m-%d'
            self.credit_memo_date = util.epoch_to_format(
                format, self.credit_memo_date)
