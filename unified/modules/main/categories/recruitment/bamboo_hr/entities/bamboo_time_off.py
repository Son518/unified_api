from dataclasses import dataclass, field
from recruitment.bamboo_hr import util

@dataclass
class BambooTimeOff():

    request_id: str = None
    status: str = None
    note: str = None
    start_date: str = None
    end_date: str = None
    include: str = None

    def __post_init__(self):
        self.start_date = util.date_to_epoch(self.start_date)
        self.end_date = util.date_to_epoch(self.end_date)
