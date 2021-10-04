from dataclasses import dataclass, field

@dataclass
class ClickSend_Send_Voice():

    to: str = None
    message: str = None
    language: str = None
    voice: str = None
    sent_from: str = None
    schedule: str = None
    custom_string: str = None
    country: str = None
