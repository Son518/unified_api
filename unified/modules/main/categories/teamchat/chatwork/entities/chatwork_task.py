from dataclasses import dataclass
from teamchat.chatwork import util


@dataclass
class ChatworkTask():

    room_id: str = None
    task_description: str = None
    end_date: str = None
    assignees: str = None
    task_id: str = None

    def __post_init__(self):
        if not(self.end_date is None or "-" in self.end_date):
            format = "%Y-%m-%d"
            self.end_date = util.epoch_to_format(format, self.end_date)
