# from unified.modules.main.categories.crm.entities.lead import Lead
from crm.entities.contact import Contact
from dataclasses import dataclass


@dataclass
class PipedriveCRMPerson(Contact):

    organization_id: str = None
    name: str = None
    visible_to: str = None
    phone: str = None
    person_id: str = None
    label_id: str = None
    