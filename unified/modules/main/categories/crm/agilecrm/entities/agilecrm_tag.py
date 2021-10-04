from dataclasses import dataclass
from crm.entities.tag import Tag


@dataclass
class AgilecrmTag(Tag):
    
    name: str = None
    contact_email: str = None
    tags: str = None
