from dataclasses import dataclass
from project_management.entities.task import Task


@dataclass
class PaymoReport():
    id: str = None
    name: str = None
    user_id: str = None
    type: str = None
    active: str = None
    share_client_id: str = None
    share_users_ids: str = None
    start_date: str = None
    end_date: str = None
    date_interval: str = None
    projects: str = None
    users: str = None
    clients: str = None
