from dataclasses import dataclass
from crm.pipedrive import util


@dataclass
class PipredriveCRMActivity():

    subject: str = None
    organization_id: str = None
    assign_to: str = None
    person_id: str = None
    deal_id: str = None
    is_done: str = None
    type: str = None
    due_date: str = None
    duration: str = None
    note: str = None
    activity_id: str = None


    def __post_init__(self):
        self.due_date_epoch()

    def due_date_epoch(self):
        if self.due_date is None or "-" in self.due_date:
            self.due_date = self.due_date
        else:
            format = "%Y-%m-%d"
            self.due_date = util.epoch_to_format(
                format, self.due_date)

