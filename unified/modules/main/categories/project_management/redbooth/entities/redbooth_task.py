from dataclasses import dataclass
from lib.util import epoch_to_format


@dataclass
class RedboothTask:
    project_id: str = None
    tasklist_id: str = None
    name: str = None
    description: str = None
    assignees: str = None
    status: str = None
    is_private: str = None
    due_on: str = None
    urgent: str = None
    due_date: str = None

    def __post_init__(self):
        if self.due_on is not None and "-" not in self.due_on:
            self.due_on = epoch_to_format("%Y-%m-%d", self.due_on)
