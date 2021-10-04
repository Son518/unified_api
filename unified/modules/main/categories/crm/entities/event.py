from dataclasses import dataclass


@dataclass
class Event:

    event_id: str = None
    name: str = None
    start_date_time: str = None
    end_date_time: str = None
    description: str = None
    owner_id: str = None
    all_day_event: bool = False
    location: str = None
    remainder_date: str = None
    related_id: str = None
