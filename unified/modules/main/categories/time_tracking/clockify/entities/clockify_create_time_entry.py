from dataclasses import dataclass
from time_tracking.clockify import util
from core.util import convert_epoch

@dataclass
class ClockifyTimeEntry():

    workspace_id: str = None
    start_datetime: str = None
    billable: str = None
    end_datetime: str = None
    project_id: str = None
    task_id: str = None
    tag_id: str = None
    description: str = None
    is_project_billable: str = None
    id: str = None
    archived: str = None
    tags: str = None
   
    def __post_init__(self):
        self.start_datetime = convert_epoch(self.start_datetime,"%Y-%m-%d")
        self.end_datetime = convert_epoch(self.end_datetime,"%Y-%m-%d")