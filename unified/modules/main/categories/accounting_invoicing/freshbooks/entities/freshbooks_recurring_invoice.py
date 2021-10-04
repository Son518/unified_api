from dataclasses import dataclass
from accounting_invoicing.freshbooks import util

@dataclass
class FreshbooksRecurringinvoice():
    
    account_id: str = None
    id: str = None
    currency_code: str = None
    date_of_issue: str = None
    days_due_from_issue: str = None
    language: str = None
    line_item_description: str = None
    line_item_name: str = None
    line_item_quantity: str = None    
    line_item_tax1_name: str = None
    line_item_tax1_percent: str = None
    line_item_unit_cost: str = None
    active_payment_gateway: str = None
    notes: str = None
    terms: str = None
    discount_amount: str = None
    discount_description: str = None
    invoice_number: str = None
    po_number: str = None
    frequency: str = None
    is_infinite: bool = True
    customerid: str = None
    create_date: str = None
    numberRecurring: str = None 

    def __post_init__(self):
        if not(self.create_date is None or "-" in self.create_date):
            format = '%Y-%m-%d'
            self.create_date = util.epoch_to_format(format, self.create_date)