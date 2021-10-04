from dataclasses import dataclass


@dataclass
class CapsulecrmCase:
    case_id: str = None
    contact_id: str = None
    name: str = None
    description: str = None
    track: str = None
    opportunity_id: str = None
    owner_id: str = None
    tags: str = None
    status: str = None
