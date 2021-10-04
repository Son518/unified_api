from crm.entities.deal import Deal
from dataclasses import dataclass
from crm.zoho_crm import util


@dataclass
class ZohocrmDeal(Deal):
    type: str = None
    owner_id: str = None
    lead_source_id: str = None

    def __post_init__(self):
        if not (self.close_date is None or "-" in self.close_date):
            format = "%Y-%m-%d"
            self.close_date = util.epoch_to_format(format, self.close_date)
