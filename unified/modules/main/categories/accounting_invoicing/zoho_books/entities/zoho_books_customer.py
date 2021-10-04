from dataclasses import dataclass

@dataclass
class ZohobooksCustomer():
    organization_id: str = None,
    place_of_contact: str = None,
    contact_name: str = None,
    company_name: str = None,
    first_name: str = None,
    last_name: str = None,
    email: str = None,
    website: str = None,
    phone: str = None,
    mobile: str = None,
    billing_address: str = None,
    billing_address_city: str = None,
    billing_address_zip: str = None,
    billing_address_state: str = None,
    billing_address_country: str = None,
    billing_address_fax: str = None,
    shipping_address: str = None,
    shipping_address_city: str = None,
    shipping_address_country: str = None,
    shipping_address_state: str = None,
    shipping_address_fax: str = None,
    shipping_address_zip: str = None,
    payment_terms: str = None,
    notes:str = None
  