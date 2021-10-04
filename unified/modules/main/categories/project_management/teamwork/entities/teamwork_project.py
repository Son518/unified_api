from dataclasses import dataclass
from project_management.entities.project import Project
from project_management.teamwork import util


@dataclass
class TeamworkProject(Project):

    first_name: str = None
    last_name: str = None
    due_date: str = None
    start_date: str = None
    end_date: str = None
    status: str = None
    tags: str = None
    tasklist_id: str = None
    owner_id: str = None
    company_id: str = None
    user_id:str =None
    category_id: str = None
    avatar: str = None
    content: str = None
    project_id: str = None

    def __post_init__(self):
        self.start_date = self.convert_epoch(self.start_date)
        self.end_date = self.convert_epoch(self.end_date)
        self.due_date = self.convert_epoch(self.due_date)
        self.created_date =  self.convert_epoch(self.created_date)

    def convert_epoch(self,date):
        if not(date is None or "-" or '' in date):
            format = "%Y-%m-%d"
            date = util.epoch_to_format(format, date).replace("-", "")
            return date
    
    