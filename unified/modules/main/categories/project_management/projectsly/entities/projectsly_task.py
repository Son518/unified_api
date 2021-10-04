from dataclasses import dataclass
from project_management.entities.task import Task


@dataclass
class ProjectslyTask(Task):
    group_id: str = None
    due_date: str = None
    priority_id: str = None
    status_id: str = None

    def __post_init__(self):
        if not (self.due_date is None or "-" in self.due_date):
            format = "%Y-%m-%d"
            self.due_date = util.epoch_to_format(format, self.due_date)
