from dataclasses import dataclass
from project_management.entities.tasklist import Tasklist

@dataclass
class Basecamp3Tasklist(Tasklist):
    todoset_id:str = None
    created_date:str = None