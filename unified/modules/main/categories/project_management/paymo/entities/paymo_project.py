from dataclasses import dataclass, field
from project_management.entities.task import Task


@dataclass
class PaymoProject():

    client_id: str = None
    project_name: str = None
    project_description: str = None
    budget_hours: str = None
    billable: str = None
    price_per_hour: str = None
    color: str = None
    team_members_id: str = None
    project_managers_id: str = None
    id: str = None
    name: str = None
    code: str = None
    task_code_increment: str = None
    description: str = None
    workflow_id: str = None
    status_id: str = None
    active: str = None
    adjustable_hours: str = None
    hourly_billing_mode: str = None
    estimated_price: str = None
    price: str = None
    invoiced: str = None
    invoice_item_id: str = None
    flat_billing: str = None
    users: str = None
    managers: str = None
    created_on: str = None
    updated_on: str = None
    client_name: str = None
    billing_type: str = None
