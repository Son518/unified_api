from dataclasses import dataclass, field
from datetime import datetime, timezone
from time_tracking.toggl import util

@dataclass
class TogglTimeEntry():

    workspace_id: str = None
    project_id: str = None
    task_id: str = None
    duration: str = None
    start_time: str = None
    stop_time: str = None
    billable: str = None
    description: str = None
    created_with: str = None
    time_entry_id: str = None

    def __post_init__(self):
        self.start_time_epoch()
        self.stop_time_epoch()

    def start_time_epoch(self):
        if not(self.start_time is None or "-" in self.start_time):
            format = "%Y-%m-%dT%H:%M:%SZ"
            self.start_time = util.epoch_to_format(format, self.start_time)

    def stop_time_epoch(self):
        if not(self.stop_time is None or "-" in self.stop_time):
            format = "%Y-%m-%dT%H:%M:%SZ"
            self.stop_time = util.epoch_to_format(format, self.stop_time)
