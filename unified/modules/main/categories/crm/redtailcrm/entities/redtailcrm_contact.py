from dataclasses import dataclass
from crm.entities.contact import Contact


@dataclass
class RedtailcrmContact(Contact):

    status: str = None
    activity_type: str = None
    category: str = None
    note_type: str = None
    draft: bool = None
    pinned: bool = None
    body: str = None
