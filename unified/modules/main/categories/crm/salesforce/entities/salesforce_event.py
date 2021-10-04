from dataclasses import dataclass
from crm.entities.event import Event


@dataclass
class SalesforceEvent(Event):

    subject: str = None
    start_date: str = None
    end_date: str = None
    name_id: str = None
    related_to: str = None
    assigned_to: str = None
