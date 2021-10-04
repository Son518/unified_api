from dataclasses import dataclass
from email_newsletters.entities.list import List


@dataclass
class AweberList(List):
    custom_fields_id: str = None
    account_id: str = None
    list_id: str = None
    email: str = None
    address: str = None
    tags: str = None
    total_subscribers: str = None
    total_unconfirmed_subscribers: str = None
