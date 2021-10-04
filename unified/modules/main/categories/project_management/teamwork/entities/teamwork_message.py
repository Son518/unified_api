from dataclasses import dataclass
from project_management.entities.task import Task


@dataclass
class TeamworkMessage(Task):

    message_id: str = None
    subject: str = None
    status: str = None
    category_id: str = None
    avatar: str = None
    tags: str = None
    body: str = None
