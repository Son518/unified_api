from dataclasses import dataclass

@dataclass
class WebflowItem():
    
    collection_id: str = None
    name: str = None
    slug: str = None
    archived: str = None
    draft: str = None
    item_id: str = None