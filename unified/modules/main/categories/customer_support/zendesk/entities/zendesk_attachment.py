from dataclasses import dataclass


@dataclass
class ZendeskAttachment():

    ticket_id: str = None
    comment: str = None
    file: str = None
