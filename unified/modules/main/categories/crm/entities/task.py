from dataclasses import dataclass


@dataclass
class Task:

    name: str = None
    due_date: str = None
    category_id: str = None
    description: str = None
    priority_id: str = None
    owner_id: str = None
    task_id: str = None
    