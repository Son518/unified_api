from dataclasses import dataclass
from project_management.entities.task import Task
from project_management.podio import util


@dataclass
class PodioItem(Task):

    due_date: str = None
    tag: str = None
    priority: str = None
    item_id: str = None
    organization_id: str = None
    workspace_id: str = None
    application_id: str = None
    attachment_url: str = None
    title: str = None
    link: str = None
    app_name: str = None
    url: str = None

    def __post_init__(self):
        if self.due_date is None or "-" in self.due_date:
            self.due_date = self.due_date
        else:
            format = "%Y-%m-%d"
            self.due_date = util.epoch_to_format(format, self.due_date)
