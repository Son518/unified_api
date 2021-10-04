from dataclasses import dataclass


@dataclass
class HubspotCompany:
    company_id: str = None
    name: str = None
    industry: str = None
    type: str = None
    city: str = None
    state: str = None
    phone: str = None
    number_of_employess: str = None
    annual_revenue: str = None
    domain: str = None
    description: str = None
