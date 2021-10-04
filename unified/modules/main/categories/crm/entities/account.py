from dataclasses import dataclass


@dataclass
class Account:

    account_id: str = None
    name: str = None
    website: str = None
    phone: str = None
    owner_id: str = None
    description: str = None
    mailing_street: str = None
    mailing_city: str = None
    mailing_state: str = None
    mailing_zip: str = None
    mailing_country: str = None
