from dataclasses import dataclass
from accounting_invoicing.quickbooks_online import util


@dataclass
class QuickbooksOnlineTimeActivity:
    date: str = None
    employee_id: str = None
    customer_id: str = None
    start_time: str = None
    end_time: str = None
    break_hours: int = 0
    break_minutes: int = 0
    hourly_rate: int = 0
    description: str = None
    time_activity_type: str = None
    vendor_id: str = None
    def __post_init__(self):
        if not(self.date is None or "-" in self.date):
            format = '%Y-%m-%d'
            self.date = util.epoch_to_format(
                format, self.date)
        if not(self.start_time is None or "-" in self.start_time):
            format = "%Y-%m-%dT%H:%M:%S-07:00"
            self.start_time = util.epoch_to_format(
                format, self.start_time)
        if not(self.end_time is None or "-" in self.end_time):
            format = "%Y-%m-%dT%H:%M:%S-07:00"
            self.end_time = util.epoch_to_format(
                format, self.end_time)
