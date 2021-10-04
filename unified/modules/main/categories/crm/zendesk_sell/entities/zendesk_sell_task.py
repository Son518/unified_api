from dataclasses import dataclass
from crm.entities.task import Task
from crm.zendesk_sell import util

@dataclass
class ZendesksellTask(Task):


    task_content: str = None
    owner:str = None
    due_date:str = None
    alert_date:str = None
    related_to:str = None
    lead:str = None

    def __post_init__(self):
        self.due_date_epoch()
        self.alert_date_epoch()
        

    def due_date_epoch(self):
        if not(self.due_date is None or "-" in self.due_date):
            format = "%Y-%m-%d"
            self.due_date = util.epoch_to_format(
                format, self.due_date)

    def alert_date_epoch(self):
        if not(self.alert_date is None or "-" in self.alert_date):
            format = "%Y-%m-%d"
            self.alert_date = util.epoch_to_format(
                format, self.alert_date)

