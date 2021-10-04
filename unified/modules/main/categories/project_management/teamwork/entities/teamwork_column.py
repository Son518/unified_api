from dataclasses import dataclass
from project_management.entities.task import Task


@dataclass
class TeamworkColumn(Task):

    column_name: str = None
    color: str = None
    id: str = None
    name: str = None
    status: str = None
    created_date: str = None
    updated_date: str = None
    project_id: str = None