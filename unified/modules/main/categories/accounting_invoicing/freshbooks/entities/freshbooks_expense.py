from dataclasses import dataclass
from accounting_invoicing.freshbooks import util

@dataclass
class FreshbooksExpense():

    account_id: str = None
    user_id: str= None
    object_id: str = None
    name: str = None
    amount: str = None
    category: str = None
    client_id: str = None
    date: str = None
    notes: str = None
    staff_member: str = None
    tax1_amount: str = None
    tax1_percent: str = None    
    tax1_name: str = None
    tax2_amount: str = None
    tax2_name: str = None
    tax2_percent: str = None
    compounded_tax: bool = True
    currency: str = None
    vendor:str = None
    duplicate_estimate: bool = True
    account_name: str = None
    transaction_id: str = None
    invoice_id: str = None
    status: str = None
    bank_name: str = None
    external_sysytem_id: str = None
    has_receipt: bool = True
    background_job_id: str = None    
    external_invoice_id: str = None
    markup_percent: str = None
    project_id: str = None
    profile_id: str = None
    visibility_state: str = None
    account_system_id: str = None

    def __post_init__(self):
        if not(self.date is None or "-" in self.date):
            format = '%Y-%m-%d'
            self.date = util.epoch_to_format(format, self.date)