from dataclasses import dataclass
from crm.entities.deal import Deal


@dataclass
class RedtailcrmDeal(Deal):

    type: str = None
