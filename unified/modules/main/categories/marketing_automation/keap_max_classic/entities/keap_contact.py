from dataclasses import dataclass
from marketing_automation.entities.contact import Contact

@dataclass
class KeapContact(Contact):

    email: str = None
    title: str = None
    job_title: str = None
    suffix: str = None
    company: str = None
    birthday: str = None
    anniversary: str = None
    phone1: str = None
    fax1: str = None
    website: str = None
    facebook: str = None
    linked_in: str = None
    twitter: str = None
    billing_address_street_line1: str = None
    billing_address_street_line2: str = None
    billing_address_city: str = None
    billing_address_state: str = None
    billing_address_zip_code: str = None
    billing_address_country: str = None
    shipping_address_street_line1: str = None
    shipping_address_street_line2: str = None
    shipping_address_city: str = None
    shipping_address_state: str = None
    shipping_address_zip_code: str = None
    shipping_address_country: str = None
    optional_address_street_line1: str = None
    optional_address_street_line2: str = None
    optional_address_city: str = None
    optional_address_state: str = None
    optional_address_zip_code: str = None
    optional_address_country: str = None
    person_notes: str = None
