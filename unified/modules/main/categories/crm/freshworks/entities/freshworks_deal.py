from dataclasses import dataclass
from crm.entities.deal import Deal


@dataclass
class FreshworksDeal(Deal):
    
    created_date: str = None
    updated_date: str = None
