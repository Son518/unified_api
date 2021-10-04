from dataclasses import dataclass
from task_management.toodledo import util
@dataclass
class ToodledoTask():

    folder_id: str = None
    context_id: str = None
    name: str = None
    due_date: str = None
    priority: str = None
    starred_task: str = None
    status: str = None
    tags: str = None
    Note: str = None

    def __post_init__(self):
        if not(self.due_date is None or "-" in self.due_date):
            format = '%Y-%m-%d'
            self.due_date = util.epoch_to_format(format, self.due_date)