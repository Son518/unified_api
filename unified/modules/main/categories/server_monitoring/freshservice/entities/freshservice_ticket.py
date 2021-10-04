from dataclasses import dataclass

@dataclass
class FreshserviceTicket:

    ticket_id: str = None
    subject: str = None
    email: str = None
    description: str = None
    priority: str = None
    status: str = None
    cc_emails: str = None
