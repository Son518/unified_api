from dataclasses import dataclass
from crm.entities.tag import Tag


@dataclass
class ZohocrmTag(Tag):
    module_id: str = None
    module_name: str = None
