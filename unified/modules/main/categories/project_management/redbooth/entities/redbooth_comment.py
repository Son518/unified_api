from dataclasses import dataclass


@dataclass
class RedboothComment:
    project_id: str = None
    tasklist_id: str = None
    task_id: str = None
    target_type: str = None
    body: str = None