from dataclasses import dataclass 
from email_newsletters.entities.segment import Segement

@dataclass
class MailjetSegment(Segment):
    x:str=None
    