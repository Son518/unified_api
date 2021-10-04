from dataclasses import dataclass
from email_newsletters.entities.campaign import Campaign

@dataclass
class SendinblueCampaign(Campaign):
    
    campaign_name:str=None
    name:str=None
    sender_id:str=None
    winner_criteria:str=None
    language:str=None
    to:str=None
    body:str=None
    cc:str = None
    bcc:str = None
    content_type:str = None
    sender:str=None
