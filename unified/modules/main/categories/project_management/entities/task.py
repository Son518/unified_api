from dataclasses import dataclass, field


@dataclass
class Task:
    id: str = None
    name: str = None
    description: str = None
    project_id: str = None
    task_id: str = None
    assigned_to: str = None
    tasklist_id:str = None