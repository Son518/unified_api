from dataclasses import dataclass


@dataclass
class MailchimpReport:
    campaign_name: str = None
    campaign_id: str = None
    audience_id: str = None
    audience_name: str = None
    subject_line: str = None
    preview_text: str = None
    emails_sent: str = None
    abuse_reports: str = None
    unsubscribed: str = None
    hard_bounces: str = None
    soft_bounces: str = None
    forwards_count: str = None
    forwards_opens: str = None
    opens_total: str = None
    clicks_total: str = None
    unique_clicks:str=None
