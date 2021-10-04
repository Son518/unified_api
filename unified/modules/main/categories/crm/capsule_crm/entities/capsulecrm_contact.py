from dataclasses import dataclass
from crm.entities.contact import Contact


@dataclass
class CapsulecrmContact(Contact):
    party_id: str = None
    title: str = None
    job_title: str = None
    tags: str = None
    website: str = None
