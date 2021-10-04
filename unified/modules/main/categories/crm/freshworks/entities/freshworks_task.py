from dataclasses import dataclass
from crm.entities.task import Task

@dataclass
class FreshworksTask(Task):

    created_date: str = None
    updated_date: str = None