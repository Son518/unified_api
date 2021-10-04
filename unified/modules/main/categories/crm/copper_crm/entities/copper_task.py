from crm.entities.task import Task
from dataclasses import dataclass


@dataclass
class CoppercrmTask(Task):
    status: str = None
    project_id: str = None
    full_name: str = None
    assignee: str = None
    remainder_date: str = None
    descrption: str = None
    priority: str = None
    tags: str = None
    related_entity_type: str = None
    related_entity_object: str = None
