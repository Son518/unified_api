from dataclasses import dataclass
from project_management.entities.project import Project


@dataclass
class ClickupFolder:
    space_id: str = None
    folder_name: str = None
    folder_id: str = None
    is_archived: bool = False
    task_count: str = None
