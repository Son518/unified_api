from dataclasses import dataclass, field
from project_management.entities.task import Task



@dataclass
class MondaydotcomGroup(Task):

    board_id: str = None
    name: str = None
    board_kind: str = None
    template_ids: str = None