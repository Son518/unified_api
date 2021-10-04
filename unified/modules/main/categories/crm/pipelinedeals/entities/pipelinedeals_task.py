from dataclasses import dataclass
from crm.entities.task import Task
from datetime import datetime, timezone
from crm.pipelinedeals import util

@dataclass
class PipelinedealsTask(Task):

    name: str = None
    description: str = None
    due_date: str = None
    association_type: str = None
    association_id: str = None
    category_id: str = None
    type: str = None

    def __post_init__(self):
        self.due_date_epoch()

    def due_date_epoch(self):
        if self.due_date is None or "-" in self.due_date:
            self.due_date = self.due_date
        else:
            format = "%Y-%m-%dT%H:%M:%SZ"
            self.due_date = util.epoch_to_format(format, self.due_date)