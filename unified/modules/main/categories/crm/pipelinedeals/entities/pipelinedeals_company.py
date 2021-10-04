from dataclasses import dataclass
from crm.entities.account import Account

@dataclass
class PipelinedealsCompany(Account):

    name: str = None
    phone: str = None
    website: str = None
    email: str = None
    company: str = None
    address: str = None
    city: str = None
    state: str = None
    postal_code: str = None
    country: str = None
    region_id: str = None
    industry_id: str = None
    company_id: str = None
    trigger: str = None
    owner_name: str = None
    user_id: str = None