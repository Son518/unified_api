from dataclasses import dataclass
from video_conferencing.clickmeeting import util

@dataclass
class ClickmeetingEvent():

    name: str = None
    room_type: str = None
    access_type: str = None
    registration: str = None
    permanent_room: str = None
    password: str = None