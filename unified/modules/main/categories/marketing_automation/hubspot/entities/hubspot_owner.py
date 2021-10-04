from dataclasses import dataclass


@dataclass
class HubspotOwner:
    owner_id: str = None
    email: str = None
    first_name: str = None
    last_name: str = None
    user_id: str = None
    archived: str = None
