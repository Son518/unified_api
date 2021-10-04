from dataclasses import dataclass
from crm.entities.task import Task
from crm.capsule_crm import util

@dataclass
class CapsulecrmTask(Task):
    def __post_init__(self):
        if not(self.due_date is None or "-" in self.due_date):
            # format = "%m-%d-%Y"
            format = '%Y-%m-%d'
            self.due_date = util.epoch_to_format(format, self.due_date)