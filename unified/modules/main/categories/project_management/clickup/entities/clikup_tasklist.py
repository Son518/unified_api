from dataclasses import dataclass
from project_management.entities.tasklist import Tasklist


@dataclass
class ClickupTasklist(Tasklist):
    folder_id: str = None
    priority: str = None
    assignee_to: str = None
    description: str = None
    due_date: str = None
