from dataclasses import dataclass
from project_management.trello import util


@dataclass
class TrelloCard:
    assigned_to: str = None
    description: str = None
    due_date: str = None
    card_id: str = None
    label_id: str = None
    name: str = None
    list_id: str = None
    attachment_url: str = None
    attachment_name: str = None
    closed: str = None

    def __post_init__(self):
        if self.due_date is None or "-" in self.due_date:
            self.due_date = self.due_date
        else:
            format = "%Y-%m-%d"
            self.due_date = util.epoch_to_format(format, self.due_date)
