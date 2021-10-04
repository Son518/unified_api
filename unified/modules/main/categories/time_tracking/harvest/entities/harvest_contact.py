from dataclasses import dataclass

@dataclass
class HarvestContact:
    contact_id: str = None
    client_id: str = None
    first_name: str = None
    last_name: str = None
    email: str = None
    title: str = None
    phone_office: str = None
    phone_mobile: str = None 
    fax: str = None