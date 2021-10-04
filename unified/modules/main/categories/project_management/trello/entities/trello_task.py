from dataclasses import dataclass
from project_management.entities.task import Task

@dataclass
class TrelloTask(Task):
    due_date: str = None
