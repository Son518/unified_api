from dataclasses import dataclass
from email_newsletters.entities.subscriber import Subscriber


@dataclass
class CampaingnmonitorSubcriber(Subscriber):
    client_id: str = None
    subscriber_id: str = None
    date: str = None
    event_type: str = None
    custom_fields: str = None
    state: str = None
    new_email: str = None
    resubscribe: bool = False
    restart_autoresponders: bool = False
