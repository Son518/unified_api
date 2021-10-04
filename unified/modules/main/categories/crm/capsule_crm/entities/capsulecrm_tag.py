from dataclasses import dataclass
from crm.entities.tag import Tag

@dataclass
class CapsulecrmTag(Tag):
    contact_id :str = None
    tag :str = None
    description:str=None