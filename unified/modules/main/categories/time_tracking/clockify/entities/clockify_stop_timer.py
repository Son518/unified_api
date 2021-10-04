from dataclasses import dataclass
from time_tracking.clockify import util
from core.util import convert_epoch

@dataclass
class ClockifyStopTimer():

    end_datetime: str = None
    workspace_id: str = None
    user_id: str = None
    project_id: str = None
   
    def __post_init__(self):
        self.end_datetime = convert_epoch(self.end_datetime,"%Y-%m-%d")    