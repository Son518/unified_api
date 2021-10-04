from dataclasses import dataclass
from project_management.entities.task import Task



@dataclass
class PaymoTasklist():

    project_id:str = None
    name:str = None
    id:str = None
    milestone:str = None
    created_on:str = None
    updated_on:str = None 
    seq:str = None
