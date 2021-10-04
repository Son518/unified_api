from dataclasses import dataclass
from project_management.entities.task import Task
from project_management.basecamp3 import util
from datetime import datetime, timezone



@dataclass
class Basecamp3Task(Task):
    due_date: str = None
    created_date:str = None

    def __post_init__(self):
        if not (self.due_date is None or "-" in self.due_date):
            format="%Y-%m-%d"
            self.due_date = util.epoch_to_format(format,self.due_date)
            
