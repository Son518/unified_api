from crm.entities.contact import Contact
from dataclasses import dataclass
from crm.entities.event import Event
from crm.agilecrm import util


@dataclass
class AgilecrmEvent(Event):

    id: str = None
    event_name: str = None
    priority: str = None
    start_date: str = None
    end_date: str = None
    start_time: str = None
    end_time: str = None

    def __post_init__(self):
        self.start_date_epoch()
        self.end_date_epoch()

    def start_date_epoch(self):
        if self.start_date is None or "-" in self.start_date:
            self.start_date = self.start_date
        else:
            format = "%Y-%m-%d"
            self.start_date = util.epoch_to_format(
                format, self.start_date)

    def end_date_epoch(self):
        if self.end_date is None or "-" in self.end_date:
            self.end_date = self.end_date
        else:
            format = "%Y-%m-%d"
            self.end_date = util.epoch_to_format(
                format, self.end_date)
