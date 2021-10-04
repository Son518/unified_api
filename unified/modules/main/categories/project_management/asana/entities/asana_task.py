from dataclasses import dataclass, field
from project_management.entities.task import Task
from datetime import datetime, timezone
from project_management.asana import util

# Asana application Specific Task entites


@dataclass
class AsanaTask(Task):
    
    task_completed: bool = False
    due_date: str = None
    tag: str = None
    priority: str = None
    section_id: str = None

    def __post_init__(self):
        if not (self.due_date is None or "-" in self.due_date):
            format = "%Y-%m-%d"
            self.due_date = util.epoch_to_format(format, self.due_date)

            