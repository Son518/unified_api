from dataclasses import dataclass


@dataclass
class SalesforceTask:

    task_id: str = None
    subject: str = None
    end_date: str = None
    name_id: str = None
    related_to: str = None
    assigned_to: str = None
    status: str = None
