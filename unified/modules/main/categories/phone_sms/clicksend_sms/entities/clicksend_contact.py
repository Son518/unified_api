from dataclasses import dataclass, field

@dataclass
class ClickSend_Contact():

    contact_list: str = None
    contact_id: str = None
    list_name: str = None
    full_name: str = None
    last_name: str = None
    phone_number: str = None
    email: str = None
    fax_number: str = None
    organization_name: str = None
    city: str = None
    state: str = None
    postal_code: str = None
    country: str = None
    custom_1: str = None
    custom_2: str = None
    custom_3: str = None
    custom_4: str = None
