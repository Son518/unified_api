  
from dataclasses import dataclass
from marketing_automation.active_campaign import util

@dataclass
class ActiveCampaignDealTask:
    deal_id: int = None
    title: str = None  
    task_id: int = None 
    assignee_id: int = None 
    note: str = None
    due_date: str = None
    task_type_id: int = None
    end_date: str = None
    task_type: str = None


    def __post_init__(self):
        self.due_date_epoch()
        self.end_date_epoch()

    def due_date_epoch(self):
        if self.due_date is None or "-" in self.due_date:
            self.due_date = self.due_date
        else:
            format = "%Y-%m-%d"
            self.due_date = util.epoch_to_format(
                format, self.due_date)

    def end_date_epoch(self):
        if self.end_date is None or "-" in self.end_date:
            self.end_date = self.end_date
        else:
            format = "%Y-%m-%d"
            self.end_date = util.epoch_to_format(
                format, self.end_date)    