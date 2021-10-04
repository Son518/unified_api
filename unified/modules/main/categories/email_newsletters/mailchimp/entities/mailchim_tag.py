from dataclasses import dataclass


@dataclass
class MailchimpTag:
    tag_id: str = None
    tag_name: str = None
