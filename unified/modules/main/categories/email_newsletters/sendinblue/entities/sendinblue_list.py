from dataclasses import dataclass
from email_newsletters.entities.list import List

@dataclass
class SendinblueList(List):

    list_id: str = None
    folder_id: str = None
    created_date: str = None
    dynamic_list: bool = False
    total_subscribers: str = None
    unique_subscribers: str = None