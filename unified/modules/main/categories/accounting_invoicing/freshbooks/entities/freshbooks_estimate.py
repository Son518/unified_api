from dataclasses import dataclass
from accounting_invoicing.freshbooks import util

@dataclass
class FreshbooksEstimate():

    account_id: str = None
    object_id: str = None
    user_id: str = None
    invoice_id: str = None
    customer_id: str = None
    create_date: str = None
    estimate_number: str = None
    organization: str = None
    first_name: str = None
    last_name: str = None
    visibility_state: str = None
    discount_value: str = None    
    currency_code: str = None
    language: str = None
    terms: str = None
    po_number: str = None
    street: str = None
    city: str = None
    province:str = None
    zip_code: str = None
    country: str = None
    estimate_id: str = None
    sent_id: str = None
    value_added_tax_name: str = None
    value_added_tax_number: str = None
    notes: str = None
    name: str = None    
    description: str = None
    type: str = None
    quantity: str = None
    unit_cost_amount: str = None
    unit_cost_code: str = None
    tax_name_1: str = None
    tax_amount_1:str = None
    tax_name_2: str = None
    tax_amount_2: str = None
    send_to_customer: bool = False
    email_recipients: str = None
    email_subject: str = None
    email_body: str = None
    action_email: bool = True

    def __post_init__(self):
        if not(self.create_date is None or "-" in self.create_date):
            format = '%Y-%m-%d'
            self.create_date = util.epoch_to_format(format, self.create_date)