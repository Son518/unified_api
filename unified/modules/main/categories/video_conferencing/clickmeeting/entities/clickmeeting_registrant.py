from dataclasses import dataclass
from video_conferencing.clickmeeting import util

@dataclass
class ClickmeetingRegistrant():

    name: str = None
    last_name: str = None
    email_address: str = None
    room_id: str = None