from dataclasses import dataclass
from accounting_invoicing.quickbooks_online import util


@dataclass
class QuickbooksonlinePayment:
    customer_id: str = None
    total_amount: str = None
    unapplied_amount: str = None
    transaction_date: str = None
    line_amount: str = None
    line_linked_invoice_id: str = None
    memo: str = None
    bill_id:str=None
    
    def __post_init__(self):
        if not(self.transaction_date is None or "-" in self.transaction_date):
            format = '%Y-%m-%d'
            self.transaction_date = util.epoch_to_format(
                format, self.transaction_date)