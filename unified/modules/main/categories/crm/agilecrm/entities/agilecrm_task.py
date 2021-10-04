from crm.entities.contact import Contact
from dataclasses import dataclass
from crm.entities.task import Task


@dataclass
class AgilecrmTask(Task):
    
    progress: str = None
    is_complete: str = None
    priority: str = None
    task_type: str = None
    status: str = None
    email: str = None
    start_date: str = None
    end_date: str = None
    due: str = None
    time: str = None
    subject: str = None

    def end_date_epoch(self):
        if self.end_date is None or "-" in self.end_date:
            self.end_date = self.end_date
        else:
            format = "%Y-%m-%d"
            self.end_date = util.epoch_to_format(
                format, self.end_date).replace("-", "")
