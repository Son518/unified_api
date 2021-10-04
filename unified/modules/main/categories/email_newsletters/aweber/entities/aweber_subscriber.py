from email_newsletters.entities.subscriber import Subscriber
from dataclasses import dataclass

@dataclass
class AweberSubscriber(Subscriber):
    subscriber_id: str = None
    city: str = None
    country :str = None
    status : str= None