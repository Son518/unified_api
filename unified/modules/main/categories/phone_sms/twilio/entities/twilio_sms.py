from dataclasses import dataclass


@dataclass
class TwilioSms(): 
    from_number: str = None
    alphanumeric_sender_id: str = None
    to_number: str = None
    message:str = None
    media_url:str = None