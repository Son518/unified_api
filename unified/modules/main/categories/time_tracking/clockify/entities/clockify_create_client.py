from dataclasses import dataclass

@dataclass
class ClockifyClient():

    name: str = None
    workspace_id: str = None
    id: str = None
    archived: str = None