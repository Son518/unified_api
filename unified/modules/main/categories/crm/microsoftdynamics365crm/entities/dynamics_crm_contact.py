from dataclasses import dataclass
from crm.entities.contact import Contact


@dataclass
class Microsoftdynamics365crmContact(Contact):

    job_title: str = None
    mobile_phone: str = None
    fax: str = None
    street_1: str = None
    street_2: str = None
    street_3: str = None
    city: str = None
    state: str = None
    zip: str = None
    country: str = None
