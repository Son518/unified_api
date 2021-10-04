from dataclasses import dataclass

@dataclass
class TeamworkInvoice():

    id: str = None
    number: str = None
    po_number: str = None
    description: str = None
    date: str = None
    status: str = None
    currency_code: str = None
    fixed_cost: str = None
    project_id: str = None
    company_id: str = None
    created_date: str = None
    updated_date: str = None