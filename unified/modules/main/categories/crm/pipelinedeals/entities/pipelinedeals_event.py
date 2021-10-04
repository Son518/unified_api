from dataclasses import dataclass
from datetime import time
from crm.entities.event import Event
from crm.pipelinedeals import util

@dataclass
class PipelinedealsEvent(Event):

    name: str = None
    description: str = None
    association_type: str = None
    association_id: str = None
    start_time: str = None
    end_time: str = None
    category_id: str = None
    type: str = None

    def __post_init__(self):
        self.start_time_epoch()
        self.end_time_epoch()

    def start_time_epoch(self):
        if self.start_time is None or "-" in self.start_time:
            self.start_time = self.start_time
        else:
            format = "%Y-%m-%dT%H:%M:%SZ"
            self.start_time = util.epoch_to_format(format, self.start_time)

    def end_time_epoch(self):
        if self.end_time is None or "-" in self.end_time:
            self.end_time = self.end_time
        else:
            format = "%Y-%m-%dT%H:%M:%SZ"
            self.end_time = util.epoch_to_format(
                format, self.end_time)