from dataclasses import dataclass

@dataclass
class TeamworkExpense():

    id: str = None
    name: str = None
    description: str = None
    date: str = None
    cost: str = None
    invoice_id: str = None
    project_id: str = None
    updated_date: str = None