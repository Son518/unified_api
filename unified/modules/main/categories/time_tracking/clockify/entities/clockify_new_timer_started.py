from dataclasses import dataclass
from time_tracking.clockify import util

@dataclass
class ClockifyTimerStarted():

    end_datetime: str = None
    workspace_id: str = None
    user_id: str = None
    project_id: str = None
    start: str = None
    description: str = None
    is_billable: str = None