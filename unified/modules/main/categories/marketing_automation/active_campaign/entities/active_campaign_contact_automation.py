from dataclasses import dataclass

@dataclass
class ActiveCampaignContactAutomation:

    automation_id: int = None  
    contact_id: int = None
    subscriber_email: str = None
    contact_type:  str = None