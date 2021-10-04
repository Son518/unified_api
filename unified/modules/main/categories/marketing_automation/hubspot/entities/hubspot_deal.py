from dataclasses import dataclass
from core.util import epoch_to_format


@dataclass
class HubspotDeal:
    deal_id: str = None
    name: str = None
    pipeline: str = None
    deal_stage: str = None
    ammount: str = None
    end_date: str = None
    deal_type: str = None
    priority: str = None
    company_id: str = None
    contact_id: str = None
    owner_id: str = None

    def __post_init__(self):
        if not(self.end_date is None or "-" in self.end_date):
            format = '%Y-%m-%d'
            self.end_date = epoch_to_format(format, self.end_date)
