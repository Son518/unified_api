from dataclasses import dataclass
from email_newsletters.entities.list import List


@dataclass
class MailchimpList(List):
    audience_id: str = None
    company: str = None
    street: str = None
    address2: str = None
    city: str = None
    state: str = None
    zip: str = None
    country: str = None
    phone: str = None
    list_id: str = None
    permission_reminder: str = None
    email_type_option: bool = False
    from_name: str = None
    from_email: str = None
    subject: str = None
    language: str = None
