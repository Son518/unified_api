from dataclasses import dataclass
from crm.entities.lead import Lead


@dataclass
class Microsoftdynamics365crmLead(Lead):

    topic: str = None
    type: str = None
    email: str = None
    country: str = None
    company: str = None
    industry: str = None
    annual_revenue: str = None
    employees: str = None
    sic_code: str = None
    currency: str = None
    street_1: str = None
    street_2: str = None
    street_3: str = None
    business_phone: str = None
    mobile_phone: str = None

    def revenue(self):
        if self.annual_revenue is not None:
            return float(self.annual_revenue)
        else:
            return None
