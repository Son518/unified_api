from dataclasses import dataclass

@dataclass
class IntercomEvent():

    email: str = None
    event_name: str = None
    created_date: str = None