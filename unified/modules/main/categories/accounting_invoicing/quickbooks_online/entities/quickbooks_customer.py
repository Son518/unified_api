from accounting_invoicing.entities.contact import Contact
from dataclasses import dataclass


@dataclass
class QuickbooksonlineCustomer(Contact):
    middle_name:str=None
    customer_id: str = None
    full_name: str = None
    display_name: str = None
    title: str = None
    company: str = None
    fax: str = None
    website: str = None
    address_line1: str = None
    address_zip_code: str = None
    address_state_code: str = None
    mobile: str = None
    billing_address_city:str=None
    billing_address_zipcode:str=None
    billing_address_country:str=None
    billing_address_street:str=None
    billing_address_state:str=None
