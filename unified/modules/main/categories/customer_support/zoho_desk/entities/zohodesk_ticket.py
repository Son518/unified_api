from dataclasses import dataclass
from customer_support.zoho_desk.util import epoch_to_format


@dataclass
class ZohodeskTicket:

    ticket_id: str = None
    organization_id: str = None
    department_id: str = None
    contact_id: str = None
    subject: str = None
    email: str = None
    phone: str = None
    description: str = None
    category: str = None
    sub_category: str = None
    status: str = None
    assignee: str = None
    due_date: str = None
    priority: str = None
    channel: str = None
    classification: str = None

    def get_as_data(self, include_none=True):
        data = {
            "departmentId": self.department_id,
            "contactId": self.contact_id,
            "subject": self.subject,
            "email": self.email,
            "phone": self.phone,
            "description": self.description,
            "category": self.category,
            "subCategory": self.sub_category,
            "status": self.status,
            "assigneeId": self.assignee,
            "priority": self.priority,
            "channel": self.channel,
            "classification": self.classification
        }

        if self.due_date:
            data['dueDate'] = epoch_to_format(self.due_date)

        if not include_none:
            data = { key : value for key, value in data.items() if value is not None }

        return data
