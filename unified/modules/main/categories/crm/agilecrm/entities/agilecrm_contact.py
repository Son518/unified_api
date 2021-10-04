from crm.entities.contact import Contact
from dataclasses import dataclass


@dataclass
class AgilecrmContact(Contact):

    id: str = None
    domain: str = None
    star_value: str = None
    lead_score: str = None
    tags: str = None
    company: str = None
    title: str = None
    business_website: str = None
    subject: str = None
    start: str = None
    end: str = None
    company_type: str = None
    company_url: str = None
    company_id: str = None
    contact_type: str = None
    company_name: str = None
    owner: str = None
    phone: str = None
    add_address: str = None
    city: str = None
    state: str = None
    pin_code: str = None
    country: str = None
