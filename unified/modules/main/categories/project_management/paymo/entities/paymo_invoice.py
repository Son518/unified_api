from dataclasses import dataclass
from project_management.entities.task import Task
from core.util import convert_epoch



@dataclass
class PaymoInvoice():

    template_id:str = None
    client_id:str = None
    status:str = None
    currency:str = None
    start_date:str = None
    due_date:str = None
    tax_percentage:str = None
    bill_to:str = None
    company_info:str = None
    footer:str = None
    notes:str = None
    out_standing:str = None
    tax_text:str = None
    tax_2:str = None
    tax_on_tax:str = None
    tax_2_tax:str = None
    pay_online:str = None
    id:str=None
    number:str =None
    title:str =None
    active:str =None
    date:str =None
    delivery_date:str =None
    subtotal:str =None
    total:str =None
    tax:str =None
    tax2:str =None
    tax_amount:str =None
    tax2_amount:str =None
    discount:str =None
    discount_amount:str =None
    discount_text:str =None
    reminder_1_sent:str =None
    reminder_2_sent:str =None
    reminder_3_sent:str =None
    created_on:str =None
    updated_on:str =None
    options:str =None
    download_token:str =None
    permalink:str =None
    pdf_link:str =None
    token:str =None
    invoice_id:str =None
    item:str =None
    description:str =None
    price_unit:str =None
    quantity:str =None
    expense_id:str =None
    apply_tax:str =None

    def __post_init__(self):
        self.start_date = convert_epoch(self.start_date,"%Y-%m-%d")
        self.due_date = convert_epoch(self.due_date,"%Y-%m-%d")