from dataclasses import dataclass
from marketing_automation.entities.contact import Contact

@dataclass
class HubspotContact(Contact):
    job_title: str = None
    lifecycle_stage: str = None
    lead_status: str = None
