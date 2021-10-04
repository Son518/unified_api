from dataclasses import dataclass

@dataclass
class ZohobooksItem():
    organization_id: str = None,
    item_id: str = None,
    description: str = None,
    rate: str = None,
    tax_percentage: str = None,
    item_name: str = None