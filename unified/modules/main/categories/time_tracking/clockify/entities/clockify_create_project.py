from dataclasses import dataclass

@dataclass
class ClockifyProject():

    name: str = None
    is_project_public: str = None
    is_project_billable: str = None
    client_id: str = None
    workspace_id: str = None