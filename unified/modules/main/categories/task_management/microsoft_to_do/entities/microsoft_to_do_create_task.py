from dataclasses import dataclass
from task_management.microsoft_to_do import util
from core.util import convert_epoch

@dataclass
class MicrosofttodoTask():

    title: str = None
    list_id: str = None
    note: str = None
    start_date: str = None
    due_date: str = None
    reminder_date: str = None
    turn_reminder_on: str = None
    importance: str = None
    task_id: str = None

    def __post_init__(self):
        self.start_date = convert_epoch(self.start_date,"%Y-%m-%d")
        self.due_date = convert_epoch(self.due_date,"%Y-%m-%d") 
        self.reminder_date = convert_epoch(self.reminder_date,"%Y-%m-%d")