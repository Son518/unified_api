from dataclasses import dataclass


@dataclass
class ChatworkRoom():

    name: str = None
    description: str = None
    icon: str = None
    members: str = None
    room_id: str = None
    text: str = None
