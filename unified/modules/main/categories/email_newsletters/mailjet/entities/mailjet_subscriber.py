from dataclasses import dataclass
from email_newsletters.entities.subscriber import Subscriber

@dataclass
class MailjetSubscriber(Subscriber):
    contact_id:str=None
    contact_list: str = None
    first_name: str = None
    country: str = None
    newsletter_sub: str = None