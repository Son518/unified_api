from dataclasses import dataclass
from project_management.entities.task import Task
from project_management.teamwork import util


@dataclass
class TeamworkMilestone(Task):

    title: str = None
    end_date: str = None
    due_on: str = None
    responsible_party_id: str = None
    milestone_id: str = None
    deadline: str = None
    status: str = None
    email: str = None
    tags: str = None
    created_date: str = None
    updated_date: str = None
    tasklists: str = None
    owner_id: str = None
    notify: str = None
    private: str = None
    remainder: str = None
    users :str = None

    def __post_init__(self):

        self.due_on_epoch()
        self.end_date_epoch()
    
    def due_on_epoch(self):

        if not(self.due_on is None or "-" in self.due_on):
            format = "%Y-%m-%d"

            # teamwork api call accepts date format as YYYYMMDD
            self.due_on = util.epoch_to_format(
                format, self.due_on).replace("-", "")
    
    def end_date_epoch(self):

        if not(self.end_date is None or "-" in self.end_date):
            format = "%Y-%m-%d"

            # teamwork api call accepts date format as YYYYMMDD
            self.end_date = util.epoch_to_format(
                format, self.end_date).replace("-", "")
