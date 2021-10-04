from dataclasses import dataclass

@dataclass
class Contact:
    contact_id: str = None
    first_name: str = None
    last_name: str = None
    email: str = None
    image_url: str = None
    created_date: str = None
    phone_number: str = None
    updated_date: str = None
    address_street:str=None
    address_street_line2:str=None
    address_state: str = None
    address_city: str = None
    address_pincode: str = None
    address_country: str = None
    company_name: str = None
    company_id: str = None
    note:str=None
