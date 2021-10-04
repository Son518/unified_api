from dataclasses import dataclass
from project_management.entities.task import Task
from project_management.podio import util


@dataclass
class PodioTask(Task):

    due_on: str = None
    organization_id: str = None
    text: str = None
    task_description: str = None
    task_id: str = None
    tag: str = None
    priority: str = None
    item_id: str = None
    workspace_id: str = None
    remainder: str = None
    responsible_user: str = None
    labels: str = None
    task_name: str = None
    assignee: str = None
    attachment_url: str = None

    def __post_init__(self):
        if self.due_on is None or "-" in self.due_on:
            self.due_on = self.due_on
        else:
            format = "%Y-%m-%d"
            self.due_on = util.epoch_to_format(format, self.due_on)
