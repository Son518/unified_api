from dataclasses import dataclass, field
from accounting_invoicing.wave import util


@dataclass
class WaveCustomer():

    customer_id: str = None
    business_id: str = None
    customer_name: str = None
    account_number: str = None
    currency: str = None
    first_name: str = None
    last_name: str = None
    email: str = None
    phone_number: str = None
    toll_free_number: str = None
    mobile_number: str = None
    fax_number: str = None
    website: str = None
    address1: str = None
    address2: str = None
    city: str = None
    country: str = None
    province: str = None
    postal_code: str = None
    shipping_contact: str = None
    shipping_delivery_instructions: str = None
    shipping_phone_number: str = None
    shipping_address1: str = None
    shipping_address2: str = None
    shipping_city: str = None
    shipping_country: str = None
    shipping_province: str = None
    shipping_pin_code: str = None
