from dataclasses import dataclass


@dataclass
class Lead:

    lead_id: str = None
    last_name: str = None
    first_name: str = None
    title: str = None
    account_id: str = None
    owner_id: str = None
    description: str = None
    street: str = None
    city: str = None
    state: str = None
    zip: str = None
    country_id: str = None
    phone: str = None
    mobile: str = None
    fax: str = None
    website: str = None
    salutation: str = None
    lead_source_id: str = None
    status_id: str = None
    email:str=None
