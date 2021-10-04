from dataclasses import dataclass
from accounting_invoicing.freshbooks import util

@dataclass
class FreshbooksOtherIncome():

    account_id: str = None
    amount: str = None
    tax_amount: str = None
    amount_code: str = None
    category_name: str = None
    name: str = None
    date: str = None
    note: str = None
    payment_type: str = None
    source: str = None    
    visibility_state: str = None
   
    def __post_init__(self):
        if not(self.date is None or "-" in self.date):
            # format = "%m-%d-%Y"
            format = '%Y-%m-%d'
            self.date = util.epoch_to_format(format, self.date)