from dataclasses import dataclass
from crm.entities.account import Account


@dataclass
class RedtailcrmAccount(Account):

    contact_id: str = None
    subject: str = None
    activity_type: str = None
    start_date: str = None
    end_date: str = None
    all_day: str = None
    location: str = None
    email_address: str = None

    def __post_init__(self):

        self.end_date_epoch()
        self.start_date_epoch()

    def end_date_epoch(self):
        
        if not(self.end_date is None or "-" in self.end_date):
            format = "%Y-%m-%d"
            self.end_date = util.epoch_to_format(format, self.end_date)

    def start_date_epoch(self):
        
        if not(self.start_date is None or "-" in self.start_date):
            format = "%Y-%m-%d"
            self.start_date = util.epoch_to_format(format, self.start_date)
