from dataclasses import dataclass
from infinity.todoist import util

@dataclass
class TodoistTask():

    project_id: str = None
    title: str = None
    note: str = None
    section_id: str = None
    assigned_to: str = None
    due_date: str = None
    priority: str = None
    project_id: str = None
    label_id: str = None
    content: str = None

    def __post_init__(self):
        # for api, convert date in app's format to epoch
        if not (self.due_date is None or "-" in self.due_date):
            # for action, convert epoch  to app's format
            format = "%Y-%m-%d"
            self.due_date = util.epoch_to_format(format, self.due_date)