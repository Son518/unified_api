from dataclasses import dataclass, field
from crm.entities.task import Task
from datetime import datetime, timezone
from crm.insightly import util

# Insightly application Specific Task entites

@dataclass
class InsightlyTask(Task):

    related_email: str = None
    completed: str = None
    status_id: str = None
    progress: str = None
    start_date: str = None
    assigned_team_id: str = None
    milestone_id: str = None
    opportunity_id: str = None
    project_id: str = None
    task_name: str = None
    date_due: str = None
    task_owner_id: str = None
    email: str = None
    assigned_to: str = None
    priority: str = None
    responsible_user_id: str = None
    reminder_date_utc: str = None
    task_visibility: str = None
    completed_date: str = None
    percent_complete: str = None
    date_created: str = None
    date_updated: str = None
    reminder_sent: str = None
    owner_visible: str = None
    stage_id: str = None
    assigned_by_user_id: str = None
    parent_task_id: str = None
    reccurence: str = None
    assigned_date: str = None
    created_user_id: str = None
    customfields: str = None
    links: str = None


    def __post_init__(self):
        self.start_date_epoch()
        self.date_due_epoch()

    def start_date_epoch(self):
        if not(self.start_date is None or "-" in self.start_date):
            format = "%Y-%m-%dT%H:%M:%SZ"
            self.start_date = util.epoch_to_format(format, self.start_date)

    def date_due_epoch(self):
        if not(self.date_due is None or "-" in self.date_due):
            format = "%Y-%m-%dT%H:%M:%SZ"
            self.date_due = util.epoch_to_format(format, self.date_due)
