from dataclasses import dataclass


@dataclass
class ZohocrmNote:
    title: str = None
    content: str = None
    parent_module: str = None
    parent_id: str = None
    owner_id: str = None
