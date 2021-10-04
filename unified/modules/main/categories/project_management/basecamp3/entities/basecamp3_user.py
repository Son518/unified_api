from dataclasses import dataclass
from project_management.entities.user import User


@dataclass
class Basecamp3User(User):
    is_admin: bool = False
    account_id: str = None
    created_date: str = None
    title: str = None
