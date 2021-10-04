from dataclasses import dataclass
from email_newsletters.entities.campaign import Campaign


@dataclass
class MailjetCampaign(Campaign):
    campaign_title: str = None
    campaign_id: str = None
    reply_name:str=None
    to:str=None
    contact_list:str=None
    email_body:str=None