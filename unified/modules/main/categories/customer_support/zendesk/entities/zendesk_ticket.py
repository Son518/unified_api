from dataclasses import dataclass
from customer_support.zendesk import util


@dataclass
class ZendeskTicket():

    subject: str = None
    description: str = None
    assignee: str = None
    collaborators: str = None
    collaborator_emails: str = None
    group: str = None
    requester_name: str = None
    requester_email: str = None
    tags: str = None
    status: str = None
    type: str = None
    due_at: str = None
    priority: str = None
    ticket_id: str = None
    new_comment: str = None
    author_id: str = None

    def __post_init__(self):
        self.due_at_epoch()

    def due_at_epoch(self):
        if not(self.due_at is None or "-" in self.due_at or self.due_at == ""):
            format = "%Y-%m-%d"
            self.due_at = util.epoch_to_format(format, self.due_at)
