from dataclasses import dataclass, field
from project_management.entities.task import Task



@dataclass
class MondaydotcomItem(Task):

    board_id: str = None
    group_id: str = None
    group_name: str = None
    group_color: str = None
    name: str = None
    item_id: str = None
    column_id: str = None
    value: str = None
    column_values: str = None
    create_labels_if_missing: bool = False
    update_value: str = None
    