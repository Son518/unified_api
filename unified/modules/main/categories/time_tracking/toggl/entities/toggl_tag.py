from dataclasses import dataclass, field
from datetime import datetime, timezone

@dataclass
class TogglTag():

    name: str = None
    workspace_id: str = None
    tag_id: str = None
