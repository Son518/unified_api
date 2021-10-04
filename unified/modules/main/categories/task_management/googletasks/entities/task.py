from dataclasses import dataclass
from lib.util import epoch_to_format


@dataclass
class Googletasks_task():
    task_list_id: str = None
    title: str = None
    notes: str = None
    due_on: str = None
    task_id: str = None
    status: str = None
    name: str = None


    def __post_init__(self):
        if self.due_on is not None:
            self.due_on = epoch_to_format("%Y-%m-%dT%H-%M-%SZ", self.due_on)