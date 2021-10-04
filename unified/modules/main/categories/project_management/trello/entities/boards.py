from dataclasses import dataclass


@dataclass
class TrelloBoard:
    organization_id: str = None
    teammember_joined: bool = False
    permission_level: str = None
    name: str = None
    description: str = None
    is_closed: str = False
    id: str = None
