from dataclasses import dataclass
from project_management.entities.task import Task


@dataclass
class PodioOrg(Task):

    name: str = None
    org_id: str = None
    url: str = None
    url_label: str = None
    status: str = None
    logo: str = None
    segment: str = None
    tier: str = None
    sales_agent_id: str = None
    domains: str = None
    role: str = None
    created_on: str = None
    created_by: str = None
    type: str = None
