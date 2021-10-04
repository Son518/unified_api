from dataclasses import dataclass
from crm.entities.deal import Deal
from crm.capsule_crm import util


@dataclass
class CapsulecrmDeal(Deal):
    payment_terms:str = None
    milestone_id: str = None
    tags: str = None

    def __post_init__(self):
        if not(self.close_date is None or "-" in self.close_date):
            format = '%Y-%m-%d'
            self.close_date = util.epoch_to_format(format, self.close_date)
