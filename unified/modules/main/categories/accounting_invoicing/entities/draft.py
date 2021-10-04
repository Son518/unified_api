from dataclasses import dataclass


@dataclass
class Draft():
    
    draft_id: str = None
    contact_id: str = None
    title: str = None
    summary: str = None
    currency: str = None
    description: str = None