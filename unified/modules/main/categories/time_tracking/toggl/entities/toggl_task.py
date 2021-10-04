from dataclasses import dataclass, field
from datetime import datetime, timezone

@dataclass
class TogglTask():

    name: str = None
    workspace_id: str = None
    project_id: str = None
    is_active: str = None
    task_id: str = None
