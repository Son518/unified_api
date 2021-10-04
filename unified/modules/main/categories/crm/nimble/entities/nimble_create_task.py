from dataclasses import dataclass
from crm.nimble import util

@dataclass
class NimbleTask():
    
    subject : str = None
    notes : str = None
    due_date : str = None

    def __post_init__(self):
        # for api, convert date in app's format to epoch
        if not (self.due_date is None or "-" in self.due_date):
            # for action, convert epoch  to app's format
            format = "%Y-%m-%dT%H:%M:%S"
            self.due_date = util.epoch_to_format(format, self.due_date)     