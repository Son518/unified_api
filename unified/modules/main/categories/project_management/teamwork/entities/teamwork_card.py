from dataclasses import dataclass

@dataclass
class TeamworkCard():
    id: str = None
    column_id: str = None
    task_id: str = None
    project_id: str = None
    status: str = None
    archived: str = None
    archived_date: str = None
    created_date: str = None
    updated_date: str = None
    name: str = None
    priority: str = None
    task_status: str = None
    parent_id: str = None
    task_list_id: str = None
    start_date: str = None
    due_date: str = None
    tags: str = None
    columns: str = None