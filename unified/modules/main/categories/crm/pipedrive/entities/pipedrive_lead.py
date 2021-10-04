# from unified.modules.main.categories.crm.entities.lead import Lead
from crm.entities.lead import Lead
from dataclasses import dataclass


@dataclass
class PipedriveCRMLead(Lead):
    
    person_id: str = None
    organization_id: str = None
    note: str = None
    label_id: list = None
    expected_close_date: str = None
    lead_value: str = None
    lead_value_currency: str = None
