from dataclasses import dataclass
from crm.entities.contact import Contact


@dataclass
class SalesforceContact(Contact):

    salutation: str = None
    title: str = None
    department: str = None
    birth_date: str = None
    reports_to: str = None
    lead_source: str = None
    phone: str = None
    homephone: str = None
    mobile: str = None
    other_mobile: str = None
    fax: str = None
    assistant: str = None
    asst_mobile: str = None
    other_street: str = None
    other_city: str = None
    other_state: str = None
    other_zip: str = None
    other_country: str = None
    languages: str = None
    level: str = None
