from dataclasses import dataclass


@dataclass
class ShopifyCustomer:
    customer_id:str = None
    first_name: str = None
    last_name: str = None
    email_address: str = None
    company_name: str = None
    street_address: str = None
    street_address_line2: str = None
    city: str = None
    state: str = None
    country: str = None
    zip_code: str = None
    phone: str = None
    tags: str = None
    note: str = None
    accepts_marketing: bool = False
    tax_exempt: bool = False
    send_email_invite: bool = False
