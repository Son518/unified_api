from dataclasses import dataclass

@dataclass
class FreshdeskTicket():
    subject: str = None
    email: str = None
    type: str = None
    description: str = None
    priority: str = None
    cc_email: str = None
    ticket_id: str = None
    notes: str = None
    private: bool = False