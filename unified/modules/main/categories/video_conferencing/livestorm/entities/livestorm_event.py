from dataclasses import dataclass
from datetime import timezone
from video_conferencing.livestorm import util

@dataclass
class LivestormEvent():

    identify: str = None
    title: str = None
    slug: str = None
    created_at: str = None
    estimated_duration: str = None
    registration_link: str = None
    published_at: str = None
    nb_registered: str = None
    room_link: str = None
    estimated_started_at: str = None
    started_at: str = None
    ended_at: str = None
    duration: str = None
    nb_attended: str = None
    attendees: str = None