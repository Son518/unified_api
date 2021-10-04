from dataclasses import dataclasses


@dataclass
class ChatworkSendmessage():

    room_id: str = None
    text: str = None
