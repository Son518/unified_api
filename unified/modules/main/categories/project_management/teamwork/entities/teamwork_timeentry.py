from dataclasses import dataclass
from project_management.entities.task import Task
from project_management.teamwork import util


@dataclass
class TeamworkTimeentry(Task):

    date: str = None
    hours: str = None
    minutes: str = None
    created_date: str = None
    updated_date: str = None
    time_entries_id: str = None

    def __post_init__(self):
        self.created_date_epoch()
        self.updated_date_epoch()

    def created_date_epoch(self):
        if not(self.created_date is None or "-" in self.created_date):
            format = "%Y-%m-%d"

            # teamwork api call accepts date format as YYYYMMDD
            self.created_date = util.epoch_to_format(
                format, self.created_date).replace("-", "")

    def updated_date_epoch(self):
        if not(self.updated_date is None or "-" in self.updated_date):
            format = "%Y-%m-%d"

            # teamwork api call accepts date format as YYYYMMDD
            self.updated_date = util.epoch_to_format(
                format, self.updated_date).replace("-", "")
