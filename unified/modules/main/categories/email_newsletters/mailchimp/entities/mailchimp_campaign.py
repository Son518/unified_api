from dataclasses import dataclass


@dataclass
class MailchimpCampaign:
    
    campaign_id:str=None
    campaign_name: str = None
    audience_id: str = None
    tag_id: str = None
    subject: str = None
    preview_text: str = None
    from_name: str = None
    from_email: str = None
    to_name: str = None
