from dataclasses import dataclass
from project_management.basecamp3 import util


@dataclass
class Basecamp3ScheduleEntry():
    id: str = None
    event_name: str = None
    event_description: str = None
    start_date: str = None
    end_date: str = None
    participant_id: str = None
    schedule_id: str = None
    project_id: str = None
    created_by: str = None
    created_date: str = None
    account_id: str = None

    def __post_init__(self):
        self.start_date_epoch()
        self.end_date_epoch()

    def start_date_epoch(self):
        if not (self.start_date is None or "-" in self.start_date):
            format = "%Y-%m-%d"
            self.start_date = util.epoch_to_format(format, self.start_date)

    def end_date_epoch(self):
        if not (self.end_date is None or "-" in self.end_date):
            format = "%Y-%m-%d"
            self.end_date = util.epoch_to_format(format, self.end_date)
