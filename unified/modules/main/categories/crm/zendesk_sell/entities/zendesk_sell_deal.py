from dataclasses import dataclass
from crm.entities.deal import Deal

@dataclass
class ZendesksellDeal(Deal):
    tag: str = None
    primary_contact: str = None
    owner: str = None
    pipeline: str = None
    stage: str = None
    deal_name: str = None
    currency: str = None
    hot: bool = False
    source: str = None
    created_date: str = None
    updated_date:str = None
    