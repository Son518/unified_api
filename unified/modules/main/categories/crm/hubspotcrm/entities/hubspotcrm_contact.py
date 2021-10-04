from dataclasses import dataclass
from crm.entities.contact import Contact


@dataclass
class HubspotcrmContact(Contact):

    updated_date: str = None
    created_date: str = None