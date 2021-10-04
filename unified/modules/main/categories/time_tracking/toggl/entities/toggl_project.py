from dataclasses import dataclass, field
from datetime import datetime, timezone

@dataclass
class TogglProject():

    name: str = None
    workspace_id: str = None
    client_id: str = None
    template_id: str = None
    is_project_private: str = None
    is_project_billable: str = None
    project_id: str = None
    is_active: str = None
