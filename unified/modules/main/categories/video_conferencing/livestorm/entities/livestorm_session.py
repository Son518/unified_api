from dataclasses import dataclass
from datetime import timezone
from video_conferencing.livestorm import util

@dataclass
class LivestormSession():

    name: str = None
    first_name: str = None
    last_name: str = None
    email: str = None
    event_id: str = None
    session_id: str = None
    referrer: str = None
    utm_source: str = None
    utm_medium: str = None
    utm_term: str = None
    utm_content: str = None
    utm_campaign: str = None
    id: str = None
    value: str = None
    type: str = None
    status: str = None
    timezone: str = None
    registrants_count: str = None
    room_link: str = None