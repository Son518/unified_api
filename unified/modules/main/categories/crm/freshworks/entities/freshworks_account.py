from dataclasses import dataclass
from crm.entities.account import Account


@dataclass
class FreshworksAccount(Account):
    
    account_name: str = None
    annual_revenue: str = None
    created_date: str = None
    updated_date: str = None
    facebook: str = None
    twitter: str = None
    linkedin: str = None
    address: str = None
    city: str = None
    state: str = None
    zipcode: str = None
    country: str = None
    industry_id: str = None
    business_phone: str = None
