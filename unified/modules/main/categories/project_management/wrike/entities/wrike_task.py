from dataclasses import dataclass
from project_management.entities.task import Task
from project_management.wrike import util


@dataclass
class WrikeTask(Task):

    event_author_id: str = None
    event_type: str = None
    updated_date: str = None
    created_date: str = None
    hours: str = None
    comment: str = None
    title: str = None
    folder_id: str = None
    subfolder_id: str = None
    task_name: str = None
    task_description: str = None
    task_type: str = None
    task_importance: str = None
    assignee: str = None
    attachment_url: str = None
    due_date: str = None
    date: str = None

    def __post_init__(self):
        # for api, convert date in app's format to epoch
        if self.date is None or "-" in self.date:
            self.date = self.date
        # for action, convert epoch  to app's format
        else:
            format = "%Y-%m-%d"
            self.date = util.epoch_to_format(format, self.date)
