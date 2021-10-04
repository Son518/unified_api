from dataclasses import dataclass


@dataclass
class RedboothSubtask:
    task_id: str = None
    project_id: str = None
    tasklist_id: str = None
    name: str = None