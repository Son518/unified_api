from dataclasses import dataclass

@dataclass
class ClockifyTask():

    name: str = None
    workspace_id: str = None
    project_id: str = None
    status: str = None
    id: str = None
    estimate: str = None
    billable: str = None