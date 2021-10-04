from dataclasses import dataclass, field
from datetime import datetime, timezone

@dataclass
class TogglClient():

    name: str = None
    workspace_id: str = None
    client_id: str = None
