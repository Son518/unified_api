from dataclasses import dataclass
from project_management.entities.comment import Comment
from project_management.teamwork import util


@dataclass
class TeamworkComment(Comment):

    body: str = None
    comment_id: str = None
    created_date: str = None
    updated_date: str = None
    updated_after_date: str = None
    user_id: str = None
    object_id: str = None
    notified_user_ids: str = None
    avatar: str = None
    tasklist_id: str = None
    content_type: str = None
    owner_id: str = None
    file_url: str = None
    notify: str = None
    private: bool = False

    def __post_init__(self):
        self.created_date = self.convert_epoch(self.created_date)
        self.updated_date = self.convert_epoch(self.updated_date)
        self.updated_after_date = self.convert_epoch(self.updated_after_date)

    def convert_epoch(self,date):
        if not(date is None or "-" or '' in date):
            format = "%Y-%m-%d"
            date = util.epoch_to_format(format, date).replace("-", "")
            return date


    
    