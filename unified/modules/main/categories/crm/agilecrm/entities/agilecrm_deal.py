from dataclasses import dataclass
from crm.entities.deal import Deal
from crm.agilecrm import util


@dataclass
class AgilecrmDeal(Deal):

    id: str = None
    expected_value: str = None
    contact_ids: str = None
    apply_discount: str = None
    discount_value: str = None
    discount_amt: str = None
    owner_email: str = None
    owner: str = None
    track_id: str = None
    milestone: str = None
    related_to: str = None
    end_date: str = None
    deal_source: str = None
    url_test: str = None
    created_date: str = None

    def __post_init__(self):
        self.created_date_epoch()
        self.end_date_epoch()

    def end_date_epoch(self):
        if self.end_date is None or "-" in self.end_date:
            self.end_date = self.end_date
        else:
            format = "%Y-%m-%d"
            self.end_date = util.epoch_to_format(
                format, self.end_date)

    def created_date_epoch(self):
        if self.created_date is None or "-" in self.created_date:
            self.created_date = self.created_date
        else:
            format = "%Y-%m-%d"
            self.created_date = util.epoch_to_format(
                format, self.created_date)
