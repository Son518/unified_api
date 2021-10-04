from dataclasses import dataclass
from crm.copper_crm import util


@dataclass
class CoppercrmActivity:
    parent_id: str = None
    parent_type: str = None
    category_type: str = None
    category_id: str = None
    description: str = None
    activity_type: str = None
    activity_date: str = None
    parent_object: str = None
    acting_user: str = None
    details: str = None


    def __post_init__(self):
        self.activity_date_epoch()

    def activity_date_epoch(self):
        if self.activity_date is None or "-" in self.activity_date:
            self.activity_date = self.activity_date
        else:
            format = "%Y-%m-%d"
            self.activity_date = util.epoch_to_format(
                format, self.activity_date)