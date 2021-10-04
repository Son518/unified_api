from dataclasses import dataclass

@dataclass
class ActiveCampaignTrackedEvent:
    event_key: str = None  
    event_account_id: str = None  ## int or str?
    event_name: str = None
    event_value: str = None  ## int, float, or str?
    contact_email_address: str = None 
    account_id: str = None