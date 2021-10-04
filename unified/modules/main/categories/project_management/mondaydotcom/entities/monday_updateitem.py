from dataclasses import dataclass, field
from project_management.entities.task import Task
from datetime import datetime, timezone
from project_management.asana import util


@dataclass
class MondaydotcomUpdateItem  (Task):

    board_id: str = None
    group_id: str = None
    itemname: str = None
    phone_number: str = None
    country_flag: str = None
    email: str = None
    email_label: str = None
    text: str = None
    new_value: str = None
    ids: str = None
    new_item_new_value: str = None
    new_value: str = None
    creator_id: str = None
    index_value: str = None
    column_type: str = None
    changed_at: str = None
    new_date_value: str = None
    new_time_value: str = None
    title: str = None
    item_id: str = None
    column_id: str = None
    column_values: str = None
    create_labels_if_missing: bool = False
    new_text_value: str = None

    def __post_init__(self):
        if self.new_date_value is None or "-" in self.new_date_value:
            self.new_date_value = self.new_date_value
        else:
            format = "%Y-%m-%d"
            self.new_date_value = util.epoch_to_format(format, self.new_date_value)