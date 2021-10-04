from dataclasses import dataclass
from task_management.any_do import util

@dataclass
class AnydoTask(): 

    name: str = None
    notes: str = None
    tags: str = None
    list_id: str = None
    assigned_to: str = None
    id: str = None
    owner: str = None
    note: str = None
    task_id: str = None
    priority: str = None
    category: str = None