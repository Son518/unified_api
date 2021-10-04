from dataclasses import dataclass

@dataclass
class PlivoSendsms():
    source_number: str = None
    destination_number: str = None
    text: str = None
    