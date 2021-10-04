from dataclasses import dataclass, field
from project_management.entities.task import Task
from datetime import datetime, timezone
from project_management.podio import util


@dataclass
class PodioApp(Task):

    status: str = None
    space_id: str = None
    link_add: str = None
    type: str = None
    name: str = None
    item_name: str = None
    usage: str = None
    external_id: str = None
    item_id = str = None,
    link: str = None
