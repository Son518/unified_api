from crm.entities.lead import Lead
from dataclasses import dataclass
from crm.nocrm_io import util


@dataclass
class NoCRMioLead(Lead):

    user_email: str = None
    tags: str = None
    creation_date: str = None
    title: str = None
    comment: str = None
    status: str = None
    step_name: str = None
    step_id: str = None
    activity_id: str = None
    amount: str = None
    probability: str = None
    close_date: str = None

    def __post_init__(self):
        self.creation_date_epoch()
        self.close_date_epoch()

    def creation_date_epoch(self):
        if not(self.creation_date is None or "-" in self.creation_date):
            format = "%Y-%m-%dT%H:%M:%S.000Z"
            self.creation_date = util.epoch_to_format(
                format, self.creation_date)

    def close_date_epoch(self):
        if not(self.close_date is None or "-" in self.close_date):
            format = "%Y-%m-%dT%H:%M:%S.000Z"
            self.close_date = util.epoch_to_format(format, self.close_date)
