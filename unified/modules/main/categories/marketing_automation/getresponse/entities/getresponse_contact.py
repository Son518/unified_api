from dataclasses import dataclass
from marketing_automation.entities.contact import Contact

@dataclass
class GetresponseContact(Contact):
    
    list_id: str = None
    name: str = None
    tags: str = None
    birthdate: str = None
    street: str = None
    city: str = None
    state: str = None
    postal_code: str = None
    country: str = None
    comment: str = None
    fax: str = None
    company: str = None
    campaignId: str = None
    email: str = None
    phone: str = None
    campaign_name: str = None