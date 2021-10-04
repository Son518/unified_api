from dataclasses import dataclass

@dataclass
class KeapCompany():

    company: str = None
    email: str = None
    phone1: str = None
    fax1: str = None
    street_address1: str = None
    street_address2: str = None
    city: str = None
    state: str = None
    postal_code: str = None
    website: str = None
    country: str = None
