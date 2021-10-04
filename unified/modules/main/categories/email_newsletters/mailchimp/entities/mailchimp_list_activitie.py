
from dataclasses import dataclass


@dataclass
class MailchimpListActivity:
    day: str = None
    emails_sent: str = None
    unique_opens: str = None
    recipient_clicks: str = None
    hard_bounce: str = None
    soft_bounce: str = None
    subs: str = None
    unsubs: str = None
    other_adds: str = None
    other_removes: str = None
