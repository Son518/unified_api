from dataclasses import dataclass
from crm.entities.deal import Deal


@dataclass
class OnpagecrmDeal(Deal):

    owner_name: str = None
    owner_email: str = None
    created_date: str = None
    updated_date: str = None
    status: str = None
