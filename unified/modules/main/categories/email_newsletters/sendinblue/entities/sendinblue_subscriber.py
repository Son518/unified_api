from dataclasses import dataclass
from email_newsletters.entities.subscriber import Subscriber


@dataclass
class SendinblueSubscriber(Subscriber):
    contact_id: str = None
    folder_id: str = None
    campaign_id: str = None
    first_name: str = None
    sms: str = None
    folder_name: str = None
    list_name: str = None
    created_date: str = None
    updated_date: str = None
