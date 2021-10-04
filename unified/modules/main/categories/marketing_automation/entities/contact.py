from dataclasses import dataclass

@dataclass
class Contact:

    contact_id: str = None
    email_address: str = None
    first_name: str = None
    last_name: str = None
    phone_number: str =None