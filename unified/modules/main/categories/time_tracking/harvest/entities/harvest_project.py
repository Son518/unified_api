from dataclasses import dataclass

@dataclass
class HarvestProject:
    project_id: str = None
    client_id: str = None
    name: str = None
    code: str = None
    bill_by: str = None
    project_billing_rate: str = None
    budget_by: str = None
    budget_amount: str = None
    notes: str = None
    is_active: str = None
    is_billable: str = None