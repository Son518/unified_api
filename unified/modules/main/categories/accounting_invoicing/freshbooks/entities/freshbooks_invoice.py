from dataclasses import dataclass
from accounting_invoicing.freshbooks import util

@dataclass
class FreshbooksInvoice():
    
    account_id: str = None
    customerid: str = None
    user_id: str = None
    object_id: str = None
    name: str = None
    invoice_id: str = None
    estimateid: str = None
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
    invoice_paid: bool = True
    terms: str = None
    discount_amount:str = None
    discount_value: str = None
    invoice_number: str = None
    po_number: str = None
    contactid: str = None
    type: str = None
    amount: str = None
    code: str = None
    owner: str = None
    presentation: str = None
    create_date: str = None
    email_recipients: str = None
    email_body: str = None
    email_subject: str = None
    action_email: bool = True
    estimate_id: str = None
    create_if_does_not_exist: bool = True
    append_line_items_on_update: bool = True
    notes: str = None
    discount_description: str = None
    body: str = None
    delay: str = None
    days: str = None
    late_fee_amount: str = None
    repeat_late_fee: str = None
    first_tax_name: str = None
    first_tax_percent: str = None
    second_tax_name: str = None
    second_tax_percent: str = None

    def __post_init__(self):
        if not(self.create_date is None or "-" in self.create_date):
            format = '%Y-%m-%d'
            self.create_date = util.epoch_to_format(format, self.create_date)