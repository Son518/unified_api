from dataclasses import dataclass
from accounting_invoicing.entities.invoice import Invoice
from accounting_invoicing.quickbooks_online import util


@dataclass
class QuickbooksonlineInvoice(Invoice):
    customer_id: str = None
    send_later: str = None
    terms: str = None
    due_date: str = None
    invoice_number: str = None
    product_id: str = None
    product_description: str = None
    message_displayed_on_invoice: str = None
    message_displayed_on_statement: str = None
    product_quantity: int = 0
    product_amount: str = None
    product_tax: str = None
    product_rate: int = 0
    invoice_date: str = None
    invoice_id: str = None
    email: str = None
    vendor_id:str=None
    transaction_date:str=None
    bill_number:str=None
    product_billable:str=None
    memo:str=None

    def __post_init__(self):
        if not(self.due_date is None or "-" in self.due_date):
            format = '%Y-%m-%d'
            self.due_date = util.epoch_to_format(
                format, self.due_date)
        if not(self.invoice_date is None or "-" in self.invoice_date):
            format = '%Y-%m-%d'
            self.invoice_date = util.epoch_to_format(
                format, self.invoice_date)
