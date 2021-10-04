from dataclasses import dataclass
from project_management.entities.task import Task
from project_management.teamwork import util


@dataclass
class TeamworkTask(Task):

    first_name: str = None
    last_name: str = None
    content: str = None
    date_created: str = None
    date_updated: str = None
    start_date: str = None
    status: str = None
    end_date: str = None
    due_date: str = None
    tag: str = None
    created_after_date: str = None
    updated_after_date: str = None
    assigned_user_ids: str = None
    parent_id: str = None
    progress: str = None
    estimated_minutes: str = None
    tags: str = None
    has_custom_fields: str = None
    milestone_id: str = None
    template_id: str = None
    avatar: str = None
    people_id: str = None
    priority: str = None
    tasklist_name: str = None
    private:bool = False
    tasklist_description:str = None
    task_name: str = None
    task_description:str = None
    subtask_description:str = None
    user_id: str = None
    owner_id:str = None
    subtask_name: str  = None
    notify: bool = None
    project_id: str = None
    board_column_id: str = None

    def __post_init__(self):
        self.start_date = self.convert_epoch(self.start_date)
        self.end_date = self.convert_epoch(self.end_date)
        self.due_date = self.convert_epoch(self.due_date)
        self.date_created = self.convert_epoch(self.date_created)
        self.created_after_date = self.convert_epoch(self.created_after_date)
        self.updated_after_date = self.convert_epoch(self.updated_after_date)


    def convert_epoch(self,date):
        if not(date is None or "-" or '' in date):
            format = "%Y-%m-%d"
            date = util.epoch_to_format(format, date).replace("-", "")
            return date

    