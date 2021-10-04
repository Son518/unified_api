from dataclasses import dataclass
from email_newsletters.entities.subscriber import Subscriber


@dataclass
class MailchimpSubscriber(Subscriber):
    segment_id:str=None
    tag_id:str=None
    note:str=None
    first_name: str = None
    last_name: str = None
    street: str = None
    address2: str = None
    city: str = None
    state: str = None
    zip: str = None
    country: str = None
    phone: str = None
    birthday: str = None
