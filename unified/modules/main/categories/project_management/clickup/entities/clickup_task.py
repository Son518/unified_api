from dataclasses import dataclass
from project_management.entities.task import Task


@dataclass
class ClickupTask(Task):
    start_date: str = None
    priority: str = None
    due_date: str = None
    list_id: str = None
    tag: str = None
