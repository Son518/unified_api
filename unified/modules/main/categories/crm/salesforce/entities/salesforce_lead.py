from dataclasses import dataclass
from crm.entities.lead import Lead


@dataclass
class SalesforceLead(Lead):

    company: str = None
    lead_source: str = None
    industry: str = None
    annual_revenue: str = None
    other_mobile: str = None
    email: str = None
    lead_status: str = None
    rating: str = None
    no_employees: str = None
    product_interest: str = None
    sic_code: str = None
    current_generator: str = None
    no_locations: str = None
    postal_code: str = None
    country: str = None
    primary: str = None
    number_of_locations: str = None
