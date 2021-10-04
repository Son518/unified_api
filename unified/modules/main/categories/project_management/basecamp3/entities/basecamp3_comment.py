from dataclasses import dataclass
from project_management.entities.comment import Comment

@dataclass
class Basecamp3Comment(Comment):
    account_id:str = None
    created_date: str = None