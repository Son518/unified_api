from dataclasses import dataclass

@dataclass
class IntercomCompany():

    company: str = None
    monthly_revenue: str = None
    plan: str = None
    tag_name: str = None
    untag: str = False