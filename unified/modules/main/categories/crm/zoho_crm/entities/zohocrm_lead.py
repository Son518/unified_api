from dataclasses import dataclass
from crm.entities.lead import Lead


@dataclass
class ZohocrmLead(Lead):
    currency_symbol:str=None
    employees: str = None
    rating_id: str = None
    company_name: str = None
    industry_id: str = None
    annual_revenue: str = None
    email: str = None
    lead_status_id: str = None
    no_of_Employees: str = None
