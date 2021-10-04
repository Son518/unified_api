from dataclasses import dataclass


@dataclass
class MailchimpMemberActivity:
    email_id: str = None
    audiance_id: str = None
    total_items: str = None
    activity: str = None
