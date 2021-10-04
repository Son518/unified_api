from dataclasses import dataclass

@dataclass
class ActiveCampaignAccount:
    account_id: int = None
    name: str = None
    website: str = None
    address_1: str = None
    address_2: str = None
    city: str = None
    state: str = None
    postal_code: str = None
    country: str = None
    phone_number: str = None
    description: str = None
    number_of_employees: str = None
    annual_revenue: str = None
    industry: str = None
    # account_url: str = None