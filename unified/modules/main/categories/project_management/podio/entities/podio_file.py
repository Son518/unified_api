from dataclasses import dataclass, field
from project_management.entities.task import Task
from datetime import datetime, timezone
from project_management.podio import util

@dataclass
class PodioFile(Task):

    due_date: str = None
    file_url: str = None

    def __post_init__(self):
        if self.due_date   is None or "-" in self.due_date:
            self.due_date = self.due_date
        else:
            format="%Y-%m-%d"
            self.due_date = util.epoch_to_format(format,self.due_date)