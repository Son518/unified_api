from dataclasses import dataclass
from accounting_invoicing.quickbooks_online import util

@dataclass
class QuickbooksonlineJournal:
    journal_date: str = None
    journal_number: str = None
    debit_account_type_id: str = None
    debit_amount: str = None
    debit_description: str = None
    debit_customer_id: str = None
    debit_vendor_id: str = None
    debit_employee_id: str = None
    credit_account_type_id: str = None
    credit_amount: str = None
    credit_description: str = None
    credit_customer_id: str = None
    credit_vendor_id: str = None
    credit_employee_id: str = None
    memo: str = None
    def __post_init__(self):
        if not(self.journal_date is None or "-" in self.journal_date):
            format = '%Y-%m-%d'
            self.journal_date = util.epoch_to_format(
                format, self.journal_date)
