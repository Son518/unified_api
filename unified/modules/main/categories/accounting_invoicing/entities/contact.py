from dataclasses import dataclass


@dataclass
class Contact():

    contact_id: str = None
    name: str = None
    first_name: str = None
    last_name: str = None
    email: str = None
    phone: str = None
    fax: str = None
    mobile: str = None
    address_attention: str = None
    address_city: str = None
    address_state: str = None
    address_postal: str = None
    address_country: str = None