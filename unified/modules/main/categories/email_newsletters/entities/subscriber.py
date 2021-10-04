from dataclasses import dataclass


@dataclass
class Subscriber:
    subscriber_id: str = None
    email: str = None
    list_id: str = None
    name: str = None
    account_id: str = None
    audience_id: str = None
    tags: str = None
    last_name: str = None
    subscriber_id: str = None