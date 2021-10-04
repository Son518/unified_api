from dataclasses import dataclass

@dataclass
class JiraservicedeskRequest:
    id: str = None
    site_id: str = None
    service_desk_id: str = None
    project_id: str = None
    type_id: str = None
    summary: str = None
    description: str = None

