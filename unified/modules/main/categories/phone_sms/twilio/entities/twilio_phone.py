from dataclasses import dataclass


@dataclass
class TwilioPhone(): 
    from_number: str = None
    to_number: str = None
    media_url: str = None
    message: str = None
    voice: str = None
    language: str = None
    send_digits: str = None
    
