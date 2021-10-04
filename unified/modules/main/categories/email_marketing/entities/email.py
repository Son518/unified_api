from dataclasses import dataclass

@dataclass
class Email:
    email: str = None
    timestamp: str = None
    event_type: str = None
