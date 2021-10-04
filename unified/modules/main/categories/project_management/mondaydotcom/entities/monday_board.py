from dataclasses import dataclass, field
from project_management.entities.task import Task



@dataclass
class MondaydotcomBoard(Task):

    board_id: str = None
    board_name: str = None
    board_kind: str = None
    item_id: str = None
    template_id: str = None
    board_tags:str = None
    group_id:str = None
    column_id:str = None
    group_title:str = None
    column_title:str = None
    groups: str = None
    columns: str = None
    project_name: str = None

