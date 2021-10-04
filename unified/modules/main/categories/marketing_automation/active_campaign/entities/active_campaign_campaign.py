from dataclasses import dataclass
from marketing_automation.entities.contact import Contact


@dataclass
class ActiveCampaignCampaign(Contact):
    email_message: str = None
    contact_list: list 
    campaign_name: str = None