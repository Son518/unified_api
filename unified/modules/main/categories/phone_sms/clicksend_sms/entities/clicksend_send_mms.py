from dataclasses import dataclass, field

@dataclass
class ClickSend_Send_MMS():

    body: str = None
    subject: str = None
    to: str = None
    schedule: str = None
    media_url: str = None
