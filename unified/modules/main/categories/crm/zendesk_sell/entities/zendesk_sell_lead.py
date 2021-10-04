from dataclasses import dataclass
from crm.entities.lead import Lead

@dataclass
class ZendesksellLead(Lead):

    lead_id:str=None
    email:str = None
    title: str = None
    company_name: str = None
    work_number: str = None
    mobile_number: str = None
    industry: str = None
    tags: str = None
    street: str = None
    city: str = None
    postal_code: str = None
    state: str = None
    country: str = None
    owner: str = None
    website: str = None
    facebook: str = None
    linkedin: str = None
    twitter: str = None
    skype: str = None
    fax_number: str = None
    source:str = None
    status:str = None
    created_date:str = None
    updated_date:str = None