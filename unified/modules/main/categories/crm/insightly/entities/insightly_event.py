from dataclasses import dataclass, field
from crm.entities.event import Event
from datetime import datetime, timezone
from crm.insightly import util

# Insightly application Specific Event entites

@dataclass
class InsightlyEvent(Event):

    reminder_sent: str = None
    date_added: str = None
    date_updated: str = None
    title: str = None
    start_date: str = None
    end_date: str = None
    event_owner_id: str = None
    reminder_date: str = None
    event_visibility: str = None
    def __post_init__(self):

        self.start_date = self.date_to_epoch(self.start_date)
        self.reminder_date = self.date_to_epoch(self.reminder_date)
        self.end_date = self.date_to_epoch(self.end_date)
        self.date_added = self.date_to_epoch(self.date_added)
        self.date_updated = self.date_to_epoch(self.date_updated)

    def date_to_epoch(self, date):
        if not(date is None or "-" in date):
            format = "%Y-%m-%dT%H:%M:%SZ"
            date = util.epoch_to_format(format, date)
            return date
