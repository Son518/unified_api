from dataclasses import dataclass

@dataclass
class IntercomContact():

    email: str = None
    full_name: str = None
    user_id: str = None
    created_date: str = None
    unsubscribed: bool = False
    lookup_email: str = None
    phone_number: str = None
    unsubscribed_from_emails: bool = False
    company: str = None    
    lead_id: str = None
    tag_name: str = None
    untag: bool = None
    lead: str = None
    note_text: str = None
    user: str = None
    admin_id:str = None
    tag_id: str = None
    id: str = None

    