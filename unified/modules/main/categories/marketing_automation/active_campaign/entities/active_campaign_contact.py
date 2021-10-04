from dataclasses import dataclass

from marketing_automation.entities.contact import Contact

@dataclass
class ActiveCampaignContact(Contact):
    list_id: str = None    
    full_name: str = None
    tags: str = None
    organization_name: str = None