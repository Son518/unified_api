from dataclasses import dataclass
from project_management.entities.user import User


@dataclass
class PodioUser(User):

    created_on: str = None
