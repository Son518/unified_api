from dataclasses import dataclass
from accounting_invoicing.freshbooks import util

@dataclass
class FreshbooksProject():

    account_id: str = None
    title: str = None
    due_date: str = None
    project_type: str = None
    fixed_price: str = None
    rate: str = None
    budget: str = None
    active: bool = True
    complete: bool = True
    billable: bool = True
    business_id: str = None
    user_id: str = None
    object_id: str = None
    name: str = None

    def __post_init__(self):
        if not(self.due_date is None or "-" in self.due_date):
            # format = "%m-%d-%Y"
            format = '%Y-%m-%d'
            self.due_date = util.epoch_to_format(format, self.due_date)