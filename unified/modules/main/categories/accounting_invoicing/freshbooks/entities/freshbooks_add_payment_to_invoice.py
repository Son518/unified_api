from dataclasses import dataclass
from accounting_invoicing.freshbooks import util

@dataclass
class FreshbooksAddPaymentToInvoice():
    
    account_id: str = None
    amount: str = None
    date: str = None
    invoice_id: str = None
    payment_type: str = None
    note: str = None
    
    def __post_init__(self):
        if not(self.date is None or "-" in self.date):
            format = '%Y-%m-%d'
            self.date = util.epoch_to_format(format, self.date)