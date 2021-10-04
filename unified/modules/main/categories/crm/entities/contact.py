from dataclasses import dataclass


@dataclass
class Contact:

    contact_id: str = None
    account_id: str = None
    last_name: str = None
    first_name: str = None
    email: str = None
    business_phone: str = None
    owner_id: str = None
    mailing_street: str = None
    mailing_city: str = None
    mailing_state: str = None
    mailing_zip: str = None
    mailing_country: str = None
    description: str = None

